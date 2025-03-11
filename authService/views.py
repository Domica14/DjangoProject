from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .serializers import UserAuthSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class Signup(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            print(User.username)
            user = User.objects.create_user(
                username=request.data.get('username'), 
                email=request.data.get('email'), 
                password=request.data.get('password'))
            user.save()
            serializer = UserAuthSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        except:
            return Response("Cant create user", status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    @csrf_exempt
    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is not None:
            serializer = UserAuthSerializer(user)
            get_token(request)
            login(request, user)
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)