from django.contrib import admin
from .models import Career

# Register your models here.

@admin.register(Career)
class AdminCareer(admin.ModelAdmin):
    list_display = ('id', 'fknamecareer', 'fkstatus', 'fkfaculty', 'fkresolution', 'arcusur', 'posgrado')
    list_filter = ('fknamecareer', )