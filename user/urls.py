from django.urls import path, include
from .views import (
    UserAuthView
)


urlpatterns = [
    path('auth/', UserAuthView.as_view()),
]