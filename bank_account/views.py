from decimal import Decimal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from .forms import CreateAccountForm, SignUpForm, TransactionForm
from .models import BankAccount, Customer, Transaction


# Create your views here.


@login_required(login_url="login")
def create_account(req):
    customer, created = Customer.objects.get_or_create(user=req.user)
    if req.method == "POST":
        form = CreateAccountForm(req.POST)

        if form.is_valid():
            print("Valid Form")
            account = BankAccount.objects.create(
                iban=form.cleaned_data.get("iban"),
                balance=form.cleaned_data.get("balance"),
            )
            customer.account = account
            customer.save()
            return redirect("account-detail", account_id=account.id)
        else:
            print("Error")
            messages.error(req, "There was an error in the form. Please correct it.")
    else:
        form = CreateAccountForm()
    return render(req, "accounts/create_account.html", {"form": form})


def account_detail(req, account_id):
    form = TransactionForm()
    account = get_object_or_404(BankAccount, id=account_id)
    transactions = Transaction.objects.filter(account=account)
    if req.method == "POST":
        form = TransactionForm(req.POST)
        if form.is_valid():
            print("Valid Form")
            if req.POST["transaction_type"] == "DEPOSIT":
                print("balance before transaction", account.balance)
                transaction = form.save(commit=False)
                transaction.account = account
                account.balance += Decimal(req.POST["amount"])
                print("new balance:", account.balance)
                account.save()
                form.save()
            elif req.POST["transaction_type"] == "WITHDRAWAL":
                account.balance -= Decimal(req.POST["amount"])
                transaction = form.save(commit=False)
                transaction.account = account
                account.save()
                form.save()
    return render(req, "accounts/detail.html", {"form": form, "account": account, "transactions":transactions})


def index(req):
    if req.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=req.user)
            account = customer.account
            return render(req, "home.html", {"account": account})
        except Customer.DoesNotExist:
            customer = None
            account = None

    return render(req, "home.html")


def custom_login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)

                return redirect("accounts-home")
    else:
        form = AuthenticationForm()
    return render(req, "accounts/login.html", {"form": form})


def custom_logout(req):
    if req.method == "GET":
        logout(req)
        return redirect("accounts-home")


def signup(req):
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user)
            return redirect("login")
    else:
        form = SignUpForm()
    return render(req, "accounts/signup.html", {"form": form})
