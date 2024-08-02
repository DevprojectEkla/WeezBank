from django.contrib.admin.utils import lookup_field
from django.contrib.auth.forms import User
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
)


from bank_account.models import BankAccount, Customer, Transaction


class TransactionSerializer(HyperlinkedModelSerializer):
    account = HyperlinkedRelatedField(
        many=False, read_only=True, view_name="api-accounts-detail", lookup_field="id"
    )

    class Meta:
        model = Transaction
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "api-transactions-detail"}}


class BankAccountSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "api-accounts-detail", "lookup_field": "id"}
        }


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
        extra_kwargs = {"url": {"view_name": "api-users-detail", "lookup_field": "pk"}}


class CustomerSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        many=False, read_only=True, view_name="api-users-detail", lookup_field="pk"
    )
    account = HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name="api-accounts-detail",
        lookup_field="id",
    )

    class Meta:
        model = Customer
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "api-customers-detail",
                "lookup_field": "user",
            }
        }
