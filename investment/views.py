from django.shortcuts import render
from .models import InvestmentPlan, Portfolio, Transaction, Notification


# Create your views here.
def investment_plans(request):
    plans = InvestmentPlan.objects.all()
    return render(request, 'investment/investment_plans.html', {'plans': plans})

def portfolio_tracking(request):
    portfolio = Portfolio.objects.get(user=request.user)
    return render(request, 'investment/portfolio_tracking.html', {'portfolio': portfolio})

def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'investment/transaction_history.html', {'transactions': transactions})

def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'investment/notifications.html', {'notifications': notifications})
