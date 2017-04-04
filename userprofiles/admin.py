from django.contrib import admin
from .models import Profile, UserProfile

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('id', 'level', 'number',)
    search_fields = ('level', )
    list_filter = ('level', )

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ('fkuser', 'fkprofile')
    search_fields = ('fkuser__name', )
    list_filter = ('fkprofile', )