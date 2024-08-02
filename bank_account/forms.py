from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import BankAccount, Transaction, generate_iban


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ["iban", "balance"]

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        if "instance" not in kwargs:
            self.fields["iban"].initial = generate_iban()


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["transaction_type", "amount"]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Required. Enter a valid email address.",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
