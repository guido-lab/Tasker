from core.api.serializers import TaskResultsSerializer
from django.db.models import query
from core.models import Task, TaskResults
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
import uuid
from rest_framework.response import Response
from rest_framework import status
from helperScripts.taskFunctions import Tasks
from helperScripts.helper_get_ip import GetIP
from threading import Thread


class TaskerExec(Tasks):

    def call_and_forget(self, request, queryset, task_uuid):
        task_name = request.data.get('task_name')
        request_params = request.data.get('params')
        db_params = queryset.params
        params = ()
        
        for model_param in db_params:
            params += (request_params[model_param['name']],)
        
        result = getattr(Tasks, task_name)(*params)
        requester_ip = GetIP.get_client_ip(request)
        
        TaskResults.objects.create(
            task=queryset, 
            task_uuid = task_uuid, 
            requester_params = request_params, 
            requester_ip = requester_ip,
            result = result
            )
        return


class TaskerAPIView(APIView):

    def post(self, request):
        task_name = request.data.get('task_name')

        if task_name:
            queryset = Task.objects.filter(name=task_name, deleted=False)
            if queryset.count() > 0:
                task_uuid = uuid.uuid4()
                Thread(target=TaskerExec.call_and_forget, args=(self, request, queryset.first(), task_uuid)).start()

                return Response({"task_id": task_uuid}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "There is no task with the given name!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Parameters are missing!"}, status=status.HTTP_400_BAD_REQUEST)


class TaskResultsViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = TaskResults.objects.all().order_by("-created_at")
	serializer_class = TaskResultsSerializer
	__basic_fields = ('id', 'task', 'task_uuid', 'requester_ip')
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	ordering_fields = __basic_fields
	filter_fields = __basic_fields
