from django.db import models
from users.models import User
# Create your models here.


class ManagerModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=100,default="manager")
    
    def __str__(self):
        return self.user.username