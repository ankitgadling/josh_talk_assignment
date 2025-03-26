"""
This module contains the views for the tasks app.
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    Viewset for the Task model.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["post"])
    def assign_users(self, request, pk=None):
        """
        Assign users to a task.
        """
        task = self.get_object()
        user_ids = request.data.get("user_ids", [])
        users = User.objects.filter(id__in=user_ids)
        if not users:
            return Response(
                {"error": "No users found"}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            task.assigned_users.set(users)
            task.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"message": "Users assigned successfully"}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["get"])
    def user_tasks(self, request):
        """
        Get tasks for a user.
        """
        user_id = request.query_params.get("user_id")
        if not user_id:
            return Response(
                {"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            tasks = user.tasks.all()
        except Task.DoesNotExist:
            return Response(
                {"error": "Tasks not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for the User model.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
