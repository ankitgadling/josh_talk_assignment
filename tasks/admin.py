"""
This file is used to register the models in the Django admin interface.
"""

from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
