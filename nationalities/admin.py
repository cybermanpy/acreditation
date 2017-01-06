from django.contrib import admin
from .models import Nationality

@admin.register(Nationality)
class AdminNationality(admin.ModelAdmin):
    list_display = ('id', 'origin',)