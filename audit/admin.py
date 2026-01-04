from django.contrib import admin
from .models import Audit

# Register your models here.
@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('action', 'group', 'performed_by', 'time_stamp')
    search_fields = ('action', 'group__name', 'performed_by__name')
    list_filter = ('time_stamp',)