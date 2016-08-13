from django.contrib import admin
from .models import NameCareer
# Register your models here.

@admin.register(NameCareer)
class AdminNameCareer(admin.ModelAdmin):
    list_display = ('id', 'description',)
    list_filter = ('description',)