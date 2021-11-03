from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'email']


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Workspace
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Task
        fields = '__all__'
