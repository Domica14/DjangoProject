from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = User.objects.get(user=request.user.id)
        serializer = UserSerializer(user)
        refresh = RefreshToken.for_user(user)
        response = Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
        response.set_cookie(key='refresh', value=str(refresh), httponly=True, max_age=60 * 60 * 24 * 7)
        response.set_cookie(key='access', value=str(refresh.access_token), httponly=True, max_age=60 * 60 * 24 * 7)
        
        return response
    
    def post(self, request):
        newUser = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'phone': request.data.get('phone'),
            'user': request.user.id
        }
        serializer = UserSerializer(data=newUser)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class EditUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def exists(self, id):
        try:
            return User.objects.get(user=id)
        except User.DoesNotExist:
            return None

    def put(self, request, user_id):
        user = self.exists(user_id)
        if user and request.user.id == user_id:
            userToEdit = {
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'phone': request.data.get('phone'),
            }
            serializer = UserSerializer(instance=user ,data=userToEdit, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("User can't be modify", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        user = self.exists(user_id)
        if user and request.user.id == user_id:
            user.delete()
            return Response("User deleted", status=status.HTTP_200_OK)
        else:
            return Response("User can't be deleted", status=status.HTTP_404_NOT_FOUND)
        
