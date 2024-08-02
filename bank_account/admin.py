from django.contrib import admin

from .models import BankAccount, Customer, Transaction

admin.site.register(BankAccount)
admin.site.register(Customer)
admin.site.register(Transaction)
# Register your models here.
