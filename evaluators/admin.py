from django.contrib import admin
from .models import Evaluator, TypesEvaluator
# Register your models here.

@admin.register(Evaluator)
class AdminEvaluator(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'fkresolution',)
    list_filter = ('fkresolution',)

@admin.register(TypesEvaluator)
class AdminTypesEvaluator(admin.ModelAdmin):
    list_display = ('id', 'fkevaluator', 'fktypeevaluator', 'fknamecareer')
    list_filter = ('fktypeevaluator', 'fknamecareer',)