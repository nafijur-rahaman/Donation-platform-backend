from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
    campaign_name=serializers.SerializerMethodField()
    creator_name=serializers.SerializerMethodField()
    donor_name=serializers.SerializerMethodField()
    def get_campaign_name(self,obj):
            return f"{obj.campaign.title}"
        
    def get_creator_name(self,obj):
            return f"{obj.campaign.creator.user.first_name} {obj.campaign.creator.user.last_name}"
    
    def get_donor_name(self,obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
        
    