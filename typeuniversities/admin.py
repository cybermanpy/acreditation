from django.contrib import admin
from .models import TypeUniversity

# Register your models here.

@admin.register(TypeUniversity)
class AdminTypeUnviversity(admin.ModelAdmin):
    list_display = ('id', 'description',)
    list_filter = ('description',)