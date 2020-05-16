from django import forms
from .models import Task
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assignedBy','assignedTo','task','dueDate','details']
        widgets = {
            'dueDate': DateInput(),
        }


