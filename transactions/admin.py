from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    # List view configuration
    list_display = ('id', 'user', 'created_at', 'amount', 'payment_status')
   
    # Adding ordering by default
    ordering = ('-created_at',)

admin.site.register(Order, OrderAdmin)
