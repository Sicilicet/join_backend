from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Task, Subtask
from .serializers import (
    TaskSerializer,
    SubtaskSerializer,
)
from rest_framework import status


class TaskItemView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        todos = Task.objects.all()
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            saved_todo = serializer.save()
            return Response({"id": saved_todo.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        todo = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = get_object_or_404(Task, pk=pk)
        todo.delete()
        return Response({"message": "erfolgreich gelöscht"})


class SubtaskView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        subtasks = Subtask.objects.all()
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubtaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        subtask = get_object_or_404(Subtask, pk=pk)
        serializer = SubtaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subtask = get_object_or_404(Subtask, pk=pk)
        subtask.delete()
        return Response({"message": "erfolgreich gelöscht"})
