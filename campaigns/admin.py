from django.contrib import admin
from .models import Campaigns, Creator, CreatorRequest
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@admin.action(description='Activate selected campaigns')
def activate_campaigns(modeladmin, request, queryset):
    for campaign in queryset.filter(status='pending'):
        # Update campaign status
        campaign.status = 'active'
        campaign.save()

        # Prepare email details
        email_subject = 'Your Campaign is Now Active'
        email_body = render_to_string('campaign_activation_email.html', {
            'user': campaign.creator.user,
            'campaign': campaign
        })

        # Send email
        try:
            email = EmailMultiAlternatives(
                subject=email_subject,
                body='',
                to=[campaign.creator.user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()
            print(f"Email sent to {campaign.creator.user.email} for campaign {campaign.title}")
        except Exception as e:
            print(f"Error sending email to {campaign.creator.user.email}: {e}")

class CampaignAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "goal_amount", "status")
    actions = [activate_campaigns]

admin.site.register(Campaigns, CampaignAdmin)
admin.site.register(Creator)
admin.site.register(CreatorRequest)



