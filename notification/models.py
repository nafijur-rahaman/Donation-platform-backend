from django.db import models
from users.models import User
from django.utils import timezone

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications',null=True,blank=True)
    name= models.CharField(max_length=200,blank=True,null=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return f'Notification for {self.user.username}'
        return 'Notification for unknown user'

   
