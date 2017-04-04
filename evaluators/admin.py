from django.contrib import admin
from .models import Evaluator, TypesEvaluator, EvaluatorUniversity
from actions import export_xls, export_csv, export_xlsx

@admin.register(Evaluator)
class AdminEvaluator(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'fkstatus', 'ci', )
    search_fields = ('firstname',)
    list_filter = ('fkstatus',)

@admin.register(TypesEvaluator)
class AdminTypesEvaluator(admin.ModelAdmin):
    list_display = ('id', 'fkevaluator', 'fktypeevaluator', 'fknamecareer', 'fkresolution')
    search_fields = ('fkevaluator__firstname', )
    list_filter = ('fktypeevaluator', 'fknamecareer',)
    actions = [export_xls, export_csv, export_xlsx]

@admin.register(EvaluatorUniversity)
class AdminEvaluatorUniversity(admin.ModelAdmin):
    list_display = ('id', 'fkevaluator', 'fkuniversity', )
    search_fields = ('fkevaluator__firtname', )
    list_filter = ('fkuniversity', )