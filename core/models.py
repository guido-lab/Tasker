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