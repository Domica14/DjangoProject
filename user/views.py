from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from user.models import UserAuth

# Create your views here.

class UserAuthView(View):
    def get(self, request):
        user = UserAuth.objects.all()
        for u in user:
            print(u.username)
        return HttpResponse("<h1>Users</h1>")
    
    def post(self, request):
        if (UserAuth.objects.get(username="test").DoesNotExist() == True):
            user = UserAuth.objects.create(username="test", password="test")
            return HttpResponse("<h1>User Created</h1>")
        else:
            print(request.META.get('CSRF_COOKIE'))
            return HttpResponse("<h1>User Already Exists</h1>")
