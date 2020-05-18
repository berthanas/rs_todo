from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from todo.models import Task
from .forms import TaskForm
from django.views.generic.edit import CreateView
from datetime import date
from django.contrib import messages

# Create your views here.
@login_required
def addTask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        messages.success(request, "Görev başarı ile eklendi")
        return redirect("index")
    return render(request,"addTask.html",{'form':form})

@login_required
def listView(request):
    tasks = Task.objects.all()
    
    return render(request, "listview.html", {"tasks":tasks})

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

@login_required
def toggleStatus(request, id):
    task = get_object_or_404(Task, id=id)
    if task.assignedTo == request.user or task.assignedBy == request.user:
        task.status = True
        task.completedDate = date.today()
        task.save()
        messages.success(request, "Görev tamamlandı olarak düzenlendi")
    return redirect("index")
        
@login_required
def toggleStatusNotCompleted(request, id):
    task = get_object_or_404(Task, id=id)
    if task.assignedTo == request.user or task.assignedBy == request.user:
        task.status = False
        task.completedDate = None
        task.save()
        messages.success(request, "Görev tamamlanmadı olarak düzenlendi")
    return redirect("index")        

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    if task.assignedTo == request.user or task.assignedBy == request.user:
        task.delete()
        messages.success(request, "Görev başarı ile silindi")
    return redirect("index")

@login_required
def updateTask(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=task)
    if task.assignedTo == request.user or task.assignedBy == request.user:
        if form.is_valid():
            task = form.save()
            messages.success(request, "Görev başarı ile güncellendi")
            return redirect("index")
    return render(request,"updateTask.html",{'form':form})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"Giriş Başarılı")
            return redirect("index")
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {'form':form})

def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış Yapıldı...")
    return redirect("index") 

@login_required
def monthly(request):
    tasks = Task.objects.all()
    
    return render(request, "monthview.html", {"tasks":tasks})