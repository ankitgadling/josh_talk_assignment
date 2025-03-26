"""
This file contains the models for the tasks app.
"""

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Model for a task.
    """

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    assigned_users = models.ManyToManyField(User, related_name="tasks", blank=True)

    def __str__(self):
        return self.name
