from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import status
from tasks.models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

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
    def exists():
        pass
    
    def get(self, request, id_task):
        pass
    
    def put(self, request, id_task):
        pass
    
    def delete(self, request, id_task):
        pass