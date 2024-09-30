from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'encoding_method')
    search_fields = ('user__username', 'encoding_method')

admin.site.register(UserProfile, UserProfileAdmin)
