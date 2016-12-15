from django.contrib import admin
from .models import Department

# Register your models here.

@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_filter = ('name',)