from django.db import models


class BlockchainTransaction(models.Model):
    transaction_id = models.CharField(max_length=255)
    sender_address = models.CharField(max_length=255)
    receiver_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Transaction {self.transaction_id}"
