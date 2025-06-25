from django.db import models
from django.contrib.auth.models import User
from pydantic import BaseModel, Field 
from typing import List, Optional
# Create your models here.

class InvestmentPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    risk_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2)
    performance_chart = models.ImageField(upload_to='charts/', blank=True, null=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_holdings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    risk_profile = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_plan = models.ForeignKey(InvestmentPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.investment_plan.name}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"