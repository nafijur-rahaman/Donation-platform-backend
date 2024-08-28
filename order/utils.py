import requests
from django.conf import settings

def validate_payment(transaction_id):
    payload = {
        'store_id': settings.SSL_COMMERZ_STORE_ID,
        'store_passwd': settings.SSL_COMMERZ_STORE_PASSWORD,
        'tran_id': transaction_id,
    }
    
    response = requests.post(settings.SSL_COMMERZ_VALIDATION_API, data=payload)
    return response.json()
