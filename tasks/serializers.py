from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['task_name', 'completed', 'date_creation', 'date_completion', 'user']
        read_only_fields = ['id']

