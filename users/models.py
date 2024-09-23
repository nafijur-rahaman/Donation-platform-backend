from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.
STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
class User(AbstractUser):
    email=models.EmailField(unique=True)
    image = CloudinaryField('image', default='dummyimage.jpg')
    profession=models.CharField(max_length=100,default="Software Engineer")
    phone_number=models.CharField(max_length=11,blank=True,null=True)
    bio=models.TextField(blank=True)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default="active")
    address=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateField(auto_now_add=True,blank=True,null=True)
    
    
  