import uuid
from django.shortcuts import render
import requests
from django.conf import settings
from django.shortcuts import redirect
from rest_framework import status,viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from campaigns.models import Campaigns
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


class OrderView(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['user','campaign']
    



class InitiatePaymentView(APIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data  # Use request.data for JSON payload
        amount = data.get('amount')
        cus_phone = data.get('cus_phone')
        cus_add1 = data.get('cus_add1')
        cus_city = data.get('cus_city')
        cus_postcode = data.get('cus_postcode')
        campaign_id = data.get('campaign_id')
        order_id = str(uuid.uuid4())  # Generate a unique order ID

        # Get the campaign
        try:
            campaign = Campaigns.objects.get(id=campaign_id)
        except Campaigns.DoesNotExist:
            return JsonResponse({'error': f'Campaign with id {cus_city} does not exist'}, status=400)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            user = request.user
            cus_name = user.username
            cus_email = user.email
        else:
          
            cus_name = "Anonymous"
            cus_email = ""  
            if not all([cus_phone, cus_add1, cus_city, cus_postcode]):
                return JsonResponse({'error': 'Missing customer details for anonymous user'}, status=400)
            user = None

        # Create an order
        order = Order.objects.create(
            user=user,
            campaign=campaign,
            amount=amount,
            transaction_id=order_id,
            payment_status='pending'
        )

        payload = {
            'store_id': settings.SSL_COMMERZ_STORE_ID,
            'store_passwd': settings.SSL_COMMERZ_STORE_PASSWORD,
            'total_amount': amount,
            'currency': 'BDT',
            'tran_id': order_id,
            'success_url': 'https://donation-platform-backend-psi.vercel.app/api/transactions/payment-success/',
            'fail_url': 'https://donation-platform-backend-psi.vercel.app/api/transactions/payment-fail/',
            'cancel_url': 'https://donation-platform-backend-psi.vercel.app/api/transactions/payment-cancel/',
            'cus_name': cus_name,
            'cus_email': cus_email,
            'cus_phone': cus_phone,
            'cus_add1': cus_add1,
            'cus_city': cus_city,
            'cus_postcode': cus_postcode,
            'cus_country': 'Bangladesh',
        }

        response = requests.post(settings.SSL_COMMERZ_SESSION_API, data=payload)

        if response.status_code == 200:
            data = response.json()
            return Response({'payment_url': data.get('GatewayPageURL')})
        return Response({'error': 'Payment initiation failed'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def payment_success(request):
    # Extract transaction ID from request GET parameters
    transaction_id = request.POST.get('tran_id')

    # Fetch the order using the transaction ID
    
    try:
        order = Order.objects.get(transaction_id=transaction_id)
    except Order.DoesNotExist:
        return render(request, 'payment_fail.html', {'error': 'Order not found'})

    # Check if payment was successful
    if order.payment_status == 'pending':
        # Update the payment status to completed
        order.payment_status = 'completed'
        order.save()

        # Update the campaign's current_amount
        campaign = order.campaign
        campaign.fund_raised += order.amount
        campaign.save()
        
        return render(request, 'payment_success.html', {'message': 'Payment completed successfully'})
    

    return render(request, 'payment_fail.html', {'error': 'Payment not completed'})
@csrf_exempt
def payment_fail(request):
    return render(request, 'payment_fail.html')
@csrf_exempt
def payment_cancel(request):
    return render(request, 'payment_cancel.html')

def validate_payment(transaction_id):
    payload = {
        'store_id': settings.SSL_COMMERZ_STORE_ID,
        'store_passwd': settings.SSL_COMMERZ_STORE_PASSWORD,
        'tran_id': transaction_id,
    }

    response = requests.post(settings.SSL_COMMERZ_VALIDATION_API, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'status': 'INVALID'}