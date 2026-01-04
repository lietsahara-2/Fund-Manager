from django.contrib import admin
from .models import Transactions, Contributions, Loans

# Register your models here.
@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('membership', 'amount', 'transaction_type', 'transacted_at')
    search_fields = ('membership__user__name', 'transaction_type')
    list_filter = ('transaction_type', 'transacted_at')

@admin.register(Contributions)
class ContributionsAdmin(admin.ModelAdmin):
    list_display = ('membership', 'amount', 'verified', 'verified_by', 'verified_at', 'payment_ref')
    search_fields = ('membership__user__name', 'payment_ref')
    list_filter = ('verified', 'verified_at')

@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    list_display = ('membership', 'amount', 'status', 'approved_by', 'approved_at', 'outstanding_balance')
    search_fields = ('membership__user__name', 'status')
    list_filter = ('status', 'approved_at')
