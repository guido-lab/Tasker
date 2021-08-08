from django.contrib import admin
from .models import Task, TaskResults

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskResults)