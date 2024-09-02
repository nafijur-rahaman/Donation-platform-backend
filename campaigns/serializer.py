from .models import Campaigns,Review,Creator,CreatorRequest

from rest_framework import serializers

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Creator
        fields='__all__'
        
class CreatorRequestSerializer(serializers.ModelSerializer):
    requester_name = serializers.SerializerMethodField()
    class Meta:
        model = CreatorRequest
        fields = '__all__'
    def get_requester_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
               
class CampaignSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()

    class Meta:
        model = Campaigns
        fields = '__all__'
        read_only_fields = ('creator',)  # Make the creator field read-only

    def get_creator_name(self, obj):
        return f"{obj.creator.user.first_name} {obj.creator.user.last_name}"

    def update(self, instance, validated_data):
        # Remove the creator from the validated data to prevent updates
        validated_data.pop('creator', None)
        return super().update(instance, validated_data)


    
class ReviewSerializer(serializers.ModelSerializer):
    
    reviewer_name=serializers.SerializerMethodField()
    class Meta:
        model=Review
        fields='__all__'
        
    def get_reviewer_name(self,obj):
        return obj.reviewer.username
    