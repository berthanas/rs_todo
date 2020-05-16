from django.contrib import admin
from todo.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','assignedTo','dueDate','status')
    list_filter = ('assignedTo','status')
