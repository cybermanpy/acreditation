from django.contrib import admin
from .models import Evaluator, TypesEvaluator
# Register your models here.

@admin.register(Evaluator)
class AdminEvaluator(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'fkstatus')
    search_fields = ('firstname',)
    list_filter = ('fkstatus',)

@admin.register(TypesEvaluator)
class AdminTypesEvaluator(admin.ModelAdmin):
    list_display = ('id', 'fkevaluator', 'fktypeevaluator', 'fknamecareer', 'fkresolution')
    search_fields = ('fkevaluator__firstname', )
    list_filter = ('fktypeevaluator', 'fknamecareer',)