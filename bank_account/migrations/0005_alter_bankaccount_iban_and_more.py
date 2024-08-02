# Generated by Django 5.0.7 on 2024-08-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "bank_account",
            "0004_alter_transaction_options_alter_bankaccount_iban_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankaccount",
            name="iban",
            field=models.CharField(
                default="FR00NDKO5IFCN6", max_length=34, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[("DEPOSIT", "Deposit"), ("WITHDRAWAL", "Withdrawal")],
                max_length=10,
            ),
        ),
    ]
