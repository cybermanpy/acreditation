from django.contrib import admin
from .models import EvalType
# Register your models here.

@admin.register(EvalType)
class AdminEvalType(admin.ModelAdmin):
    list_display = ('id', 'description',)
    list_filter = ('description',)