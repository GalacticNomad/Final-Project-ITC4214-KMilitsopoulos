from django.contrib import admin
from .models import Profile


# Defines a custom ModelAdmin class for the Profile model
# Specifies the fields to be displayed in the admin list view

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_moderator')

# Registers the Profile model with the custom ProfileAdmin class to the admin site
admin.site.register(Profile, ProfileAdmin)
