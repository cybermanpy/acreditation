from django.contrib import admin
from .models import Evaluator, TypeEvaluator
# Register your models here.

@admin.register(Evaluator)
class AdminEvaluator(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'fkresolution',)
    list_filter = ('fkresolution',)

@admin.register(TypeEvaluator)
class AdminTypeEvaluator(admin.ModelAdmin):
    list_display = ('id', 'fkevaluator', 'fkevaltype', 'fknamecareer')
    list_filter = ('fkevaltype', 'fknamecareer',)