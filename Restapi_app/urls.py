from django.urls import path
from .views import BlockchainTransactionListCreateView, BlockchainTransactionDetailView

urlpatterns = [
        # List and Create API
        path('api/transactions/', BlockchainTransactionListCreateView.as_view(), name='transaction-list-create'),
        
        # Retrieve, Update, and Delete API
        path('api/transactions/1/', BlockchainTransactionDetailView.as_view(), name='transaction-detail'),
        
]

