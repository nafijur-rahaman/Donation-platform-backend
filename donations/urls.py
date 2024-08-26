from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DonationView,ConfirmDonationView

router=DefaultRouter()
router.register('list',DonationView)

urlpatterns = [
    path("",include(router.urls)),
    path('confirm-donation/<int:donation_id>/',ConfirmDonationView.as_view(),name='confirm-donation')
]
