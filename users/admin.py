from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    # Fields to be displayed in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Fields to be displayed in the detail view (edit page)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email','phone_number','bio','status','image','profession','address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Fields to be displayed in the filter sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # Fields for search functionality
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Fields to be used in the create/edit form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

# Unregister the default UserAdmin

# Register the customized UserAdmin
admin.site.register(User, UserAdmin)
