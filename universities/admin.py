from django.contrib import admin
from .models import University
from .actions import export_csv

@admin.register(University)
class AdminUniversity(admin.ModelAdmin):
    list_display = ('name', 'fktypeuniversity', )
    list_filter = ('fktypeuniversity', )
    actions = [export_csv, ]