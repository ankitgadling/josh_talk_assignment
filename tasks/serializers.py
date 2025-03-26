"""
Serializers for the Task and User models.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """

    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "task_type",
            "completed_at",
            "status",
            "assigned_users",
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "tasks"]
