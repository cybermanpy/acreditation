from django.contrib import admin
from .models import Name
# Register your models here.

@admin.register(Name)
class AdminName(admin.ModelAdmin):
	list_display = ('id', 'name',)
	list_fileter = ('name',)