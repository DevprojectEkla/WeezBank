from django.urls import path, include
from api.views import (
    CustomerViewSet,
    BankAccountViewSet,
    UserViewSet,
    TransactionViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("accounts", BankAccountViewSet, basename="api-accounts")
router.register("transactions", TransactionViewSet, basename="api-transactions")
router.register("users", UserViewSet, basename="api-users")

router.register("customers", CustomerViewSet, basename="api-customers")
urlpatterns = [
    path("", include(router.urls)),
]
