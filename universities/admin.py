from django.contrib import admin
from .models import University

# Register your models here.

@admin.register(University)
class AdminUniversity(admin.ModelAdmin):
    list_display = ('name', )