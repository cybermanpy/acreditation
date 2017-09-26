from django.contrib import admin
from .models import Faculty
from .actions import export_csv

@admin.register(Faculty)
class AdminFaculty(admin.ModelAdmin):
    list_display = ('id', 'fkname', 'fkuniversity', 'fkcampus', )
    list_filter = ('fkuniversity', )
    actions = [export_csv, ]