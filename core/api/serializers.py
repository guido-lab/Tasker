from core.models import Task, TaskResults
from rest_framework import serializers



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", ]


class TaskResultsSerializer(serializers.ModelSerializer):
    task = TaskSerializer()

    class Meta:
         model = TaskResults
         fields = ["id", 'task_uuid', 'task', 'requester_params', 'requester_ip', 'result', 'created_at']
