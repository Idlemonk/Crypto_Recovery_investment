# Generated by Django 5.1.1 on 2025-04-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_blockchaintransaction_contact_walletrecovery"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="subject",
        ),
        migrations.AddField(
            model_name="contact",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="privacy_policy",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="contact",
            name="type_of_recovery",
            field=models.CharField(
                choices=[
                    ("wallet", "Wallet Recovery"),
                    ("crypto", "Cryptocurrency Recovery"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=50,
            ),
        ),
    ]
