from django.contrib import admin
from .models import Campaigns,Creator,CreatorRequest
# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display=("title",'type','goal_amount','status')
    
    
    
admin.site.register(Campaigns,CampaignAdmin)
admin.site.register(Creator)
admin.site.register(CreatorRequest)



