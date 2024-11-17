from django.urls import path,include
from .views import InitiatePaymentView, payment_success, payment_fail, payment_cancel,OrderView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("list",OrderView)


urlpatterns = [
    path('',include(router.urls)),
    path('initiate-payment/', InitiatePaymentView.as_view(), name='initiate_payment'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-fail/', payment_fail, name='payment_fail'),
    path('payment-cancel/', payment_cancel, name='payment_cancel'),
]
