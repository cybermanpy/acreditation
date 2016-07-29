from django.contrib import admin
from .models import Resolution

# Register your models here.

@admin.register(Resolution)
class AdminResolution(admin.ModelAdmin):
    list_display = ('id', 'number', 'start_date', 'end_date', 'document',)
    list_filter = ('number',)