from django.db import models
from django.conf import settings

# Create your models here.
class Contributions(models.Model):
    membership = models.ForeignKey('groups.Memberships', on_delete=models.PROTECT, related_name="contributions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contributed_at = models.DateTimeField(auto_now_add=True)
    period = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)
    verified_by =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="verified_contributions", null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    payment_ref = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.membership.user.name} - {self.amount} ({self.period})"
    
class Loans(models.Model):
    membership = models.ForeignKey('groups.Memberships', on_delete=models.PROTECT, related_name="loans")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    requested_at = models.DateTimeField(auto_now_add=True)
    repayment_period = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="approved_loans", null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    disbursed_at = models.DateTimeField(null=True, blank=True)
    repayment_terms = models.TextField(null=True, blank=True)
    outstanding_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Loan for {self.membership.user.name} - {self.amount} ({self.status})"
    
class Transactions(models.Model):
    membership = models.ForeignKey('groups.Memberships', on_delete=models.PROTECT, related_name="membership_transactions") #related_name 1
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=[('contribution', 'Contribution'), ('loan_disbursement', 'Loan Disbursement'), ('loan_repayment', 'Loan Repayment'), ('investment', 'Investment')])
    transacted_at = models.DateTimeField(auto_now_add=True)
    transacted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="performed_transactions") #related names must be different as they point to same model
    reference = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} for {self.membership.user.name} by {self.transacted_by.name}"    
