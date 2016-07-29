from django.contrib import admin
from .models import Campus

# Register your models here.

@admin.register(Campus)
class AdminCampus(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)