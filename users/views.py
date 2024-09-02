from django.shortcuts import render,redirect
from rest_framework import generics,viewsets,status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer,UserRegistrationSerializer,UserLoginSerializer,ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class UserRegistrationView(generics.CreateAPIView):
    serializer_class=UserRegistrationSerializer
    
    def perform_create(self, serializer):
        user=serializer.save()
        token=default_token_generator.make_token(user)
        uid=urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link=f"https://donation-platform-backend-rmqk.onrender.com/api/users/activate/{uid}/{token}/"
        email_subject="Confrim You Registration"
        email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
        email=EmailMultiAlternatives(email_subject,'',to=[user.email])
        email.attach_alternative(email_body,'text/html')
        email.send()
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': 'Registration successful! Please check your email to confirm your registration.'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST) 


def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
        
    except(User.DoesNotExist):
        user=None
        
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True 
        user.save()
        return redirect('https://donation-platform.netlify.app/login.html')
    else:
        return redirect('https://donation-platform.netlify.app/register.html')
    
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
                   
                        user_id=auth_user.id
                        token, _ = Token.objects.get_or_create(user=auth_user)
                        login(request,auth_user)
                        return Response({
                            'token':token.key,
                            'user_id':user_id
                        })
                    except User.DoesNotExist:
                        return Response("User not found")
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
        
        
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response({"detail": "User account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)    


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