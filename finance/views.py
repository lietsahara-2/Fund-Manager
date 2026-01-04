from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Contributions, Loans, Transactions
from .serializers import ContributionsSerializer, LoansSerializer, TransactionsSerializer
#importing for custom actions
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from groups.models import Memberships
from .utils import log_audit

# Create your views here.
class ContributionsModelViewSet(viewsets.ModelViewSet):
    queryset = Contributions.objects.all()
    serializer_class = ContributionsSerializer
    permission_classes = [IsAdminUser]
    # Custom action to approve a contribution. decorator used to define custom endpoint
    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser]) #detail=True ensures it applies on 1 object instead of list
    def approve(self, request,pk=None):
        contributions=self.get_object()
        contributions.verified=True
        contributions.verified_by=request.user
        contributions.verified_at=timezone.now()
        contributions.save()

        #saving transaction record for the approved contribution
        Transactions.objects.create(
        membership=contributions.membership,
        amount=contributions.amount,
        transaction_type='contribution',
        transacted_by=request.user,
        reference=contributions.payment_ref
    )   
        #saving audit log
        log_audit("contribution created", contributions, request.user)

        return Response({'status':'contribution approved'})


class LoansModelViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        loan = self.get_object()
        loan.status = 'approved'
        loan.approved_by = request.user
        loan.approved_at = timezone.now()
        loan.outstanding_balance = loan.amount  #initializing outstanding balance
        loan.save()
            
        #saving transaction record for loan disbursement
        Transactions.objects.create(
        membership=loan.membership,
        amount=loan.amount,
        transaction_type='loan_disbursement',
        transacted_by=request.user,
        reference=loan.reference)

        #saving audit log
        log_audit("Approved Loan", loan, request.user)

        return Response({'status': 'loan approved'})

        # Additional custom action to reject a loan
    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        loan = self.get_object()
        loan.status = 'rejected'
        loan.approved_by = request.user
        loan.approved_at = timezone.now()
        loan.save()

        log_audit("Rejected Loan", loan, request.user)

        return Response({'status': 'loan rejected'})
    
    #Admin doesn't edit transactions directly, so no viewset for Transactions
    #all transactions are created via contributions and loans for financial integrity
        
            

# Users can only view and create their own contributions and loans
class ContributionsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contributions.objects.all()
    serializer_class = ContributionsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            membership = Memberships.objects.get(user=self.request.user)
        except Memberships.DoesNotExist:
            raise serializers.ValidationError("You must be a member of a group to make a contribution.")
        serializer.save(membership=membership)

class LoansListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            membership = Memberships.objects.get(user=self.request.user)
        except Memberships.DoesNotExist:
            raise serializers.ValidationError("You must be a member of a group to request a loan.")
        serializer.save(membership=membership)

class TransactionsListAPIView(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]

#The financial group the app is created for allows users to view all transactions thus, no filtering by user is applied here
# Users can view all transactions in this version (no per-user filtering)



