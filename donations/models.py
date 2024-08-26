from django.db import models
import datetime
from campaigns.models import Campaigns
from users.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your models here.
class Donation(models.Model):
    campaigns=models.ForeignKey(Campaigns,on_delete=models.CASCADE,related_name='donations')
    donor=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_anonymous=models.BooleanField(default=False)
    confirmed=models.BooleanField(default=False)
    
    def confirm(self,email):
        if not self.confirmed:
            self.confirmed=True
            self.campaigns.fund_raised+=self.amount
            self.campaigns.save()
            self.save()
            self.send_confirmation_email(email)
            
    def send_confirmation_email(self,email):
        if self.donor and self.donor.email:
            email_subject="Donate Amount Confirm"
            email_body=render_to_string('confirm_donation_email.html',{
                'donor_username':self.donor.username,
                'donation_amount':self.amount,
                'campaign_title':self.campaigns.title,
                'current_year':datetime.datetime.now().year
            })
            email=EmailMultiAlternatives(email_subject,"",to=[email])
            email.attach_alternative(email_body,'text/html')
            email.send()
        
    
    
    def __str__(self):
        return f"{self.donor.username} donated {self.amount}BDT to this {self.campaigns.title}"