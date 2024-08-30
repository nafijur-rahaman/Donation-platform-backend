from django.utils import timezone
from django.db.models import Case, When, Value, CharField,IntegerField
from rest_framework.filters import OrderingFilter
from .models import Campaigns,Review,Creator,CreatorRequest
from .serializer import CampaignSerializer,ReviewSerializer,CreatorSerializer,CreatorRequestSerializer
from rest_framework import viewsets,status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
# Create your views here.

class CampaignView(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['type', 'status', 'creator']
    ordering_fields = ['status']
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            creator = Creator.objects.get(user=user)
        except Creator.DoesNotExist:
            raise ValidationError("Creator profile not found for the current user.")
        
        serializer.save(creator=creator)

    
        
class ReviewView(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
        
        
        
class CreatorView(viewsets.ModelViewSet):
    queryset=Creator.objects.all()
    serializer_class=CreatorSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['user_id']
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    
    
class CreatorRequestView(viewsets.ModelViewSet):
    queryset=CreatorRequest.objects.all()
    serializer_class=CreatorRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['user_id']
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
                'success': True,
                'message': 'Application submit successfully! Please check your email to confirm!.'
            }, status=status.HTTP_201_CREATED)
    
    
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        previous_status = instance.status

        response = super().update(request, *args, **kwargs)

        instance.refresh_from_db()

        if instance.status == 'approved' and previous_status != 'approved':
            instance.approve()
            self.send_approval_email(instance)
            return Response('Congratulation! Your application accepted')
        elif instance.status=='rejected' and previous_status!='rejected':
            instance.reject()
            self.send_reject_email(instance)
            return Response('Your application is rejected')
        
            

        return Response("Successfully update the status")
    
    
    
    
    def send_approval_email(self, user):
        email_subject = "Your Creator Request has been Approved!"
        context = {
            'user': user.user,
            'current_year': timezone.now().year
        }
        email_body = render_to_string('confirm_request_email.html', context)
        email = EmailMultiAlternatives(email_subject, '', to=[user.user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()
        
    
    
       
    def send_reject_email(self, user):
        email_subject = "Your Creator Request has been Rejected!"
        context = {
            'user': user.user,
            'current_year': timezone.now().year
        }
        email_body = render_to_string('reject_email.html', context)
        email = EmailMultiAlternatives(email_subject, '', to=[user.user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()
        
        
   
        
   





