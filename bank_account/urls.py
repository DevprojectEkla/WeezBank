from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="accounts-home"),
    path(
        "detail/<uuid:account_id>/",
        views.account_detail,
        name="account-detail",
    ),
    path("create/", views.create_account, name="create"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
]
