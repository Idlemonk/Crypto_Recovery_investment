from rest_framework import serializers
from .models import BlockchainTransaction

class BlockchainTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainTransaction
        fields = '__all__'  # Include all fields in the API
