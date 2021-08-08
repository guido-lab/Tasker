from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    params = models.JSONField(encoder=None, decoder=None)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name="Task"
        verbose_name_plural="Tasks"

    def __str__(self):
        return self.name


class TaskResults(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_uuid = models.CharField(max_length=50, unique=True)
    requester_params = models.JSONField(encoder=None, decoder=None)
    requester_ip = models.CharField(max_length=50)
    result = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name="TaskResults"
        verbose_name_plural="TaskResults"

    def __str__(self):
        return self.task_uuid

