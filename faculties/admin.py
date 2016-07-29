from django.contrib import admin
from .models import Faculty

# Register your models here.

@admin.register(Faculty)
class AdminFaculty(admin.ModelAdmin):
	list_display = ('name', 'fkuniversity',)
	list_filter = ('fkuniversity',)