from django.urls import path
from .views import investment_plans, portfolio_tracking, transaction_history, notifications

urlpatterns = [
    path('investment/plans/', investment_plans, name='investment_plans'),
    path('portfolio/', portfolio_tracking, name='portfolio_tracking'),
    path('transactions/', transaction_history, name='transaction_history'),
    path('notifications/', notifications, name='notifications'),
]
