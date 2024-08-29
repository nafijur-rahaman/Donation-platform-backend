from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
    campaign_name=serializers.SerializerMethodField()
    creator_name=serializers.SerializerMethodField()
    def get_campaign_name(self,obj):
            return f"{obj.campaign.title}"
        
    def get_creator_name(self,obj):
            return f"{obj.user.first_name} {obj.user.last_name}"
        
    