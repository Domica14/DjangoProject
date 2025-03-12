from django.db import models
from django.conf import settings
from django.utils import timezone
from user.models import User
import uuid

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    date_creation = models.DateTimeField(default=timezone.now)
    date_completion = models.DateTimeField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.task_name
    
    class Meta:
        db_table = 'tasks'