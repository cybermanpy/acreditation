from django.contrib import admin
from .models import Career
from actions import export_xls, export_csv, export_xlsx

# Register your models here.

@admin.register(Career)
class AdminCareer(admin.ModelAdmin):
    list_display = ('id', 'national', 'fknamecareer', 'fkstatus', 'fkfaculty', 'fkresolution', 'arcusur', 'posgrado')
    list_filter = ('fknamecareer', 'fkstatus', 'fkfaculty__fkuniversity__fktypeuniversity')
    search_fields = ('fkfaculty__fkuniversity__name', )
    actions = [export_xls, export_csv, export_xlsx]