# Generated by Django 3.0.6 on 2020-05-15 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completedDate',
            field=models.DateField(null=True, verbose_name='Tamamlanma Tarihi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='Kimden'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignedTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL, verbose_name='Kime'),
        ),
    ]
