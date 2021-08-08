from django.db.models import query
from core.models import Task
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class TaskerAPIView(APIView):
        # permission_classes = [permissions.IsAuthenticated]

		# def get_object(self, pk):
		# 	try:
		# 		return Task.objects.get(pk=pk, deleted=False)
		# 	except MemberRole.DoesNotExist:
		# 		raise Http404

        def get(self, request):
            task_name = request.data.get('task_name')
            params = request.data.get('params')
            print(task_name)
            print(params)
            if task_name and params:
                queryset = Task.objects.filter(name=task_name, deleted=False).first()
                # serializer = MemberRoleSerializer(memberRole)
                if queryset.count() > 0:
                    pass

                return Response({})
            else:
                return Response({"error": ""}, status=status.HTTP_400_BAD_REQUEST)