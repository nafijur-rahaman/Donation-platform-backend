from django.shortcuts import render,redirect
from rest_framework import generics,viewsets,status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ManagerModel
from users.models import User
from .serializer import UserSerializer,UserLoginSerializer,ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token


# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset=ManagerModel.objects.all()
    serializer_class=UserSerializer
    
    
    

    
class UserLoginView(APIView):
    
    def post(self,request):
        serializer=UserLoginSerializer(data=self.request.data)
        
        
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            
            user=User.objects.filter(email=email).first()
            if user:
                
                auth_user=authenticate(username=user.username,password=password)
            
                if auth_user:
                    try:
                   
                        manager_data = ManagerModel.objects.get(user=auth_user)
                        print(manager_data)
                        manager_id = manager_data.user.id
                        print(manager_id)
                        token, _ = Token.objects.get_or_create(user=auth_user)
                        login(request,auth_user)
                        return Response({
                            'token':token.key,
                            'user_id':manager_id,
                        })
                    except ManagerModel.DoesNotExist:
                        return Response("Manager not found")
                else:
                    return Response("Check Your email and password")
        return Response(serializer.errors)
                    
class UserLogoutView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                token = Token.objects.get(user=request.user)
                token.delete()
            except Token.DoesNotExist:
                pass 
            logout(request)
            return Response({
                'success': True,
                'message': 'Logout successful'
            }, status=status.HTTP_201_CREATED)
        else:
               return Response({
                'success': False,
                'message': 'You are not logged in or some error happened'
            }, status=status.HTTP_201_CREATED)
        


class ChangePasswordApiView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)