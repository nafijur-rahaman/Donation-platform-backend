from django.db import models
from campaigns.models import Campaigns
import uuid
from users.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)  # Link to the Campaign
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount in BDT
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
   
    

    def __str__(self):
        return f"Order {self.id} - {self.campaign.title} - {self.amount} BDT"


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
