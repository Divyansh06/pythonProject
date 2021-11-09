from django.db import models
from django.contrib.auth.models import User


class Workspace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=2000)
    image_url = models.URLField()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    image_url = models.URLField()
    category = models.CharField(max_length=255)
    is_completed = models.BooleanField()
    is_archived = models.BooleanField()
    is_deleted = models.BooleanField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
