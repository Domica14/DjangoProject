from django.urls import path, include
from .views import (
    UserView,
    EditUserView
)


urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<int:user_id>', EditUserView.as_view()),
]