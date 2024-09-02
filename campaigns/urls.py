from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *

router=DefaultRouter()
router.register('list',CampaignView)
router.register('review',ReviewView)
router.register('creator',CreatorView)
router.register('creator-request',CreatorRequestView)


urlpatterns = [
    path('',include(router.urls)),
  
]
