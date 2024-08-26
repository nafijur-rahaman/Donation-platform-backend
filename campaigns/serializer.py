from .models import Campaigns,Review,Creator,CreatorRequest

from rest_framework import serializers

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Creator
        fields='__all__'
        
class CreatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorRequest
        fields = '__all__'
               
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model=Campaigns
        fields='__all__'
        
    creator_name=serializers.SerializerMethodField()
    def get_creator_name(self, obj):
        return f"{obj.creator.user.first_name} {obj.creator.user.last_name}"

    
class ReviewSerializer(serializers.ModelSerializer):
    
    reviewer_name=serializers.SerializerMethodField()
    class Meta:
        model=Review
        fields='__all__'
        
    def get_reviewer_name(self,obj):
        return obj.reviewer.username
    