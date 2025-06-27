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


def crypto_etf_view(request):
    context ={
        "title": "BTC & ETH ETF Investment",
        "btc_etf": {
            "name": "Bitcoin ETF (BTC ETF)",
            "description": (
                "A Bitcoin ETF is an exchange-traded fund that tracks the price of Bitcoin. "
                "Instead of directly purchasing BTC, investors can buy shares in ETF which is regulated and traded on traditional stock exchanges."
                "It allows exposure to Bitcoin's performance without managing digital wallets or crypto custody."
            ),

        },
        "eth_etf": {
            "name": "Ethereum ETF (ETH ETF)",
            "description": (
                "An Ethereum ETF tracks the price of Ether, the native cryptocurrency of the Ethereum network. "
                "Like BTC ETFs, ETH ETFs are traded on regulated exchange and provide institutional and retail investors with a secure, legal, and familiar investmentinto Ethereum."
            ),
        },
        "sale_info": (
            "We offer the opportunity to invest in both BTC and ETH ETF through our regulated sales platform. "
        )    "These regulated-traded funds (RTFs) are fully compliant with industry standards, providing transparency and safety to our investors. "
        "image_url": "static/images/etf-banner.png", #Replace with actual image path
    }
    return render (request, "crypto_etf.html", context)
      