from django.contrib import admin
from .models import Career

# Register your models here.

@admin.register(Career)
class AdminCareer(admin.ModelAdmin):
    list_display = ('id', 'name', 'fkstatus', 'fkfaculty', 'fkresolution')
    list_filter = ('fkfaculty', )