from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import DonationSerializer
from django.shortcuts import get_object_or_404
from .models import Donation
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# Create your views here.


class DonationView(viewsets.ModelViewSet):
    queryset=Donation.objects.all()
    serializer_class=DonationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)


class ConfirmDonationView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request,donation_id):
        donation=get_object_or_404(Donation,id=donation_id,creator=request.user)
        
        if donation.confirmed:
            return JsonResponse("Payment already confirmed")
        else:
            donation.confirm(donation.donor.email)
        return JsonResponse("Payment confirm Successfully")
            
    
    