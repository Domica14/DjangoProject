from django.urls import path, include
from .views import (
    UserView
)


urlpatterns = [
    path('getData/', UserView.as_view()),
]