from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    donor_name=serializers.SerializerMethodField()
    campaigns_title=serializers.SerializerMethodField()
    class Meta:
        model=Donation
        fields="__all__"
    
    def get_donor_name(self,obj):
        return f"{obj.campaigns.creator.user.first_name} {obj.campaigns.creator.user.last_name}"
    
    def get_campaigns_title(self,obj):
        return obj.campaigns.title