from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserView,UserLoginView,UserLogoutView,ChangePasswordApiView
router=DefaultRouter()
router.register('list',UserView)



urlpatterns = [
    path('',include(router.urls)),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),

    
    
]
