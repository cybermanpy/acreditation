from django.contrib import admin
from .models import Status

# Register your models here.

@admin.register(Status)
class AdminStatus(admin.ModelAdmin):
    list_display = ('id', 'description',)