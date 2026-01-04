from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'date_joined')
    search_fields = ('name', 'email')
    list_filter = ('is_active', 'date_joined')
