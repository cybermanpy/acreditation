from django.contrib import admin
from .models import Faculty

# Register your models here.

@admin.register(Faculty)
class AdminFaculty(admin.ModelAdmin):
	list_display = ('id', 'name', 'fkuniversity', 'fkcampus')
	list_filter = ('fkuniversity',)