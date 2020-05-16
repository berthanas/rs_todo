from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Task(models.Model):
    # Yapılacaklar modeli, atanma tarihi, deadline, kime atandığı, kimin atadığı ve görev
    assignedTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignee", verbose_name='Kime')
    assignedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manager", verbose_name='Kimden')
    assignedDate = models.DateField(auto_now_add=True, verbose_name="Atama Tarihi")
    dueDate = models.DateField(verbose_name="Miat")
    task = models.CharField(max_length=200, verbose_name="Görev")
    details = models.TextField(verbose_name="Açıklamalar")
    status = models.BooleanField(verbose_name="Durum", default=False)
    completedDate = models.DateField(verbose_name="Tamamlanma Tarihi", null=True)

    @property
    def is_past_due(self):
        return date.today() > self.dueDate

    def __str__(self):
        return self.task
    
