from django.contrib import admin
from .models import TypeEvaluator
# Register your models here.

@admin.register(TypeEvaluator)
class AdminTypeEvaluator(admin.ModelAdmin):
    list_display = ('id', 'description',)
    list_filter = ('description',)