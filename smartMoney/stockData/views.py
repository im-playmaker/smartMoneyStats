from django.shortcuts import render
from .models import Stock

# Create your views here.
def stock(request):
    items = Stock.objects.all()
    return render(request, "stock.html", {"stocks": items})