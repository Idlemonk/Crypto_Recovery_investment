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

def crypto_investment_view(request):
    investment_packages = [
        {
            "name" : "Bitcoin ETF (BTC ETF)",
            "description": "Invest in Bitcoin through a regulated Exchange-Traded Funds that track the price of Bitcoin.",
            "risk_level": "Medium",
            "min_investment": $700
        },
        {
            "name" : "Ethereum ETF (ETH ETF)",
            "description": "Invest in regulated Exchange-Traded Funds that track the price of Ethereum.",
            "risk_level": "Medium",
            "min_investment": $500
        },
    ]

    context ={
        "title": "Crypto Investment Website_name",
        "packages": investment_packages,
    }

    return render(request, "investment/crypto_investment.html", context)