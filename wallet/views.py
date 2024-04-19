from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from TradingView_Chart.urls import *
from wallet.models import *
from django.shortcuts import redirect
from django.urls import reverse

class WalletView(APIView):
    def get(self, request):
        self.request.GET.get('userid')
        wallet = Wallet.objects.first()
        price_options = PriceTable.objects.all()
        return render(request, 'add_money.html', {'prices': price_options, 'wallet': wallet})
    
    def post(self, request):
        data = request.data
        price_id = data.get('price_id')
        wallet = Wallet.objects.first()
        price_options = PriceTable.objects.get(pk = price_id)
        wallet.balance += price_options.amount
        wallet.save()

        return redirect(reverse('wallet') + '?success=true')