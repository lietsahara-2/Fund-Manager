from rest_framework import serializers
from .models import Contributions, Loans, Transactions

class ContributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributions
        fields = "__all__"
        read_only_fields = ['membership',
                            'verified',
                            'verified_by',
                            'verified_at'
                            ]

class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"
        read_only_fields = ['membership',
                            'outstanding_balance',
                            'approved_by',
                            'approved_at',
                            'disbursed_at'
                            ]

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"
        read_only_fields = ['membership',
                            'transacted_at',
                            'transacted_by'
                            ]