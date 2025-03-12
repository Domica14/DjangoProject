from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import status
from tasks.models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone


# Create your views here.

class TaskView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            userId = request.data.get('userId')
            tasks = Task.objects.filter(user=userId)
            serializedTasks = []
            for task in tasks:
                serializedTasks.append(TaskSerializer(task).data)
            return Response(serializedTasks, status=status.HTTP_200_OK)
        except:
            return Response("Couldn't retieve any data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            task = {
                'task_name': request.data.get('taskName'),
                'user': request.data.get('userId'),
            }
            print(request.data.get('userId'))
            serializer = TaskSerializer(data=task)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response("Can't create any task", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditTaskView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def exists(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None
    
    def get(self, request, task_id):
        try:
            task = self.exists(task_id)
            if task:
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Task not found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Couldn't retieve any data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, task_id):
        try:
            task = self.exists(task_id)
            if task:
                taskToEdit = {
                    'task_name': request.data.get('taskName') if request.data.get('taskName') is not None else task.task_name,
                    'completed': request.data.get('completed') if request.data.get('completed') is not None else task.completed,
                    'date_completion': timezone.now() if request.data.get('completed') and task.date_completion is None else None,
                }
                serializer = TaskSerializer(instance=task ,data=taskToEdit, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Task not found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Couldn't retieve any data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, task_id):
        try:
            task = self.exists(task_id)
            if task:
                task.delete()
                return Response("Task deleted", status=status.HTTP_200_OK)
            else:
                return Response("Task not found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Couldn't retieve any data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)