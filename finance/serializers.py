from rest_framework import serializers
from .models import Contributions, Loans, Transactions

class ContributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributions
        fields = "__all__"

class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"