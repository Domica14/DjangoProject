from django.urls import path
from tasks.views import (
    TaskView,
    EditTaskView
)

urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('/tasks/<uuid:id_task>', EditTaskView.as_view())
]