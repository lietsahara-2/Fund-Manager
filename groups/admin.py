from django.contrib import admin

# Register your models here.
from .models import Group, Memberships

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin', 'currency', 'created_at')
    search_fields = ('name', 'admin__name')
    list_filter = ('currency',)

@admin.register(Memberships)
class MembershipsAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'joined_on', 'is_active', 'contribution_amount')
    search_fields = ('user__name', 'group__name')
    list_filter = ('is_active',)
