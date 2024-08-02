import uuid
from django.db import models
from django.contrib.auth.models import User
import string
import random


def generate_iban():
    country_code = "FR"
    check_digits = "00"
    bban = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{country_code}{check_digits}{bban}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    account = models.OneToOneField(
        "BankAccount", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.user.username


class BankAccount(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    iban = models.CharField(max_length=34, unique=True, default=generate_iban())
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Account {self.id} - IBAN {self.iban}"


class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10, choices=[("DEPOSIT", "Deposit"), ("WITHDRAW", "Withdraw")]
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type}- {self.amount}"
