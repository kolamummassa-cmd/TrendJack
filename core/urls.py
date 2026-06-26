

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.home, name="home"),
    path("check-wallet/", views.check_wallet, name="check_wallet"),
]