from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Contributions, Loans, Transactions
from .serializers import ContributionsSerializer, LoansSerializer, TransactionsSerializer

# Create your views here.
class ContributionsModelViewSet(viewsets.ModelViewSet):
    queryset = Contributions.objects.all()
    serializer_class = ContributionsSerializer
    permission_classes = [IsAdminUser]

class LoansModelViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAdminUser]

class TransactionsModelViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAdminUser]

# Users can only view
class ContributionsListAPIView(generics.ListAPIView):
    queryset = Contributions.objects.all()
    serializer_class = ContributionsSerializer
    permission_classes = [IsAuthenticated]

class LoansListAPIView(generics.ListAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAuthenticated]

class TransactionsListAPIView(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]
