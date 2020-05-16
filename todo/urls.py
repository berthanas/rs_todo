from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    path('addTask', views.addTask, name='addTask'),
    path('toggleStatus/<int:id>', views.toggleStatus, name='toggleStatus'),
    path('toggleStatusNotCompleted/<int:id>', views.toggleStatusNotCompleted, name='toggleStatusNotCompleted'),
    path('deleteTask/<int:id>', views.deleteTask, name='deleteTask'),
    path('updateTask/<int:id>', views.updateTask, name='updateTask'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('monthly', views.monthly, name='monthly')
]