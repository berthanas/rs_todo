from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from todo.models import Task
import datetime
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        today = datetime.date.today()
        tasksExpired = Task.objects.filter(assignedTo = request.user, dueDate__lt = today, status=False)
        tasksDue = Task.objects.filter(assignedTo = request.user, dueDate__gt = today, status=False)
        tasksToday = Task.objects.filter(assignedTo = request.user, dueDate = today, status=False)
        tasksCompleted = Task.objects.filter(assignedTo = request.user, status=True)
        return render(request, "index.html", {'tasksExpired':tasksExpired, 'tasksDue':tasksDue, 'tasksToday':tasksToday, 'tasksCompleted':tasksCompleted})
    
    return render(request, "index.html")


