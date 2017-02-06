from django.contrib import admin
from .models import Audit

@admin.register(Audit)
class AdminAudit(admin.ModelAdmin):
    list_display = ('id', 'action', 'username', 'logs', 'date')
    list_filter = ('action',)
    search_fields = ('date',)