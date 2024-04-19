from django.urls import path
from . import views

from wallet.models import Wallet

urlpatterns = [
    path('', views.WalletView.as_view(), name='wallet'),
]