from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'donor', 'amount','created_at')
 
  

admin.site.register(Donation, DonationAdmin)


