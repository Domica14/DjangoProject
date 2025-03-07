from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json

# Create your views here.
class Signup(View):

    def post(self, request):
        body = json.loads(request.body)
        user = User.objects.create_user(
            username=body['username'], 
            email=body['email'], 
            password=body['password'])
        user.save()
        return render(request, 'login.html')
    
    def get(self, request):
        return render(request, 'signup.html')
    

class Login(View):
    
    def get(self, request):
        body = json.loads(request.body)
        user = authenticate(username=body['username'], password=body['password'])
        if user is not None:
            return HttpResponse("<h1>Login Success</h1>", status=200)
        else:
            return HttpResponse("<h1>Login Failed</h1>", status=401)