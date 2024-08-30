from django.urls import path,include
from .views import NotificationView, mark_notification_as_read,get_unread_count
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("list",NotificationView)
urlpatterns = [
    path("", include(router.urls)),
    path('notifications/<int:notification_id>/read/', mark_notification_as_read, name='notification-mark-read'),
    path('unread-count/', get_unread_count, name='get_unread_count'),
]
