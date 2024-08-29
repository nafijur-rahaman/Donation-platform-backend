from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserView,UserProfileView,UserRegistrationView,UserLoginView,UserLogoutView,activate,DeleteUserView,ChangePasswordApiView
router=DefaultRouter()
router.register('list',UserView)



urlpatterns = [
    path('',include(router.urls)),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("activate/<uid64>/<token>/", activate, name="activate"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),
    path('delete-account/', DeleteUserView.as_view(), name='delete-account'),
    
    
]
