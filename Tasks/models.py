from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User,related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, blank=True, null=True, default='Pending')
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    