from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BlockchainTransaction
from .serializers import BlockchainTransactionSerializer

# Create your views here.

# List and Create API
class BlockchainTransactionListCreateView(ListCreateAPIView):
    queryset = BlockchainTransaction.objects.all()
    serializer_class = BlockchainTransactionSerializer

# Retrieve, Update, and Delete API
class BlockchainTransactionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BlockchainTransaction.objects.all()
    serializer_class = BlockchainTransactionSerializer
    """_summary_
    """