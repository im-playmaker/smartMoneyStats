from django.shortcuts import render
from .models import Stock

from dateutil.relativedelta import relativedelta
import time
import datetime as dt
# import from the APi
from nasdaq_data import nasdaq_grabber as ng
my_ng = ng()
my_ng.nasdaq_stocks(10)

 # print(my_ng.nasdaq_stocks(50).symbol, my_ng.nasdaq_stocks(50).netchange)
#today
# t = dt.date.today().replace(day=1)
#one year ago
# t0= t - relativedelta(years=1)
# isoformat
#iso_t0, iso_t = t0.isoformat(), t.isoformat()
#print(my_ng.nasdaq_historical_price('AAPL', iso_t0, iso_t))

# create a collection of symbols
symbols = []

for item in my_ng.nasdaq_stocks(10).symbol:
    symbols.append(item)

print("symbols ", symbols)
data = my_ng.nasdaq_stocks(10).to_dict('records')
# Create your views here.
def stock(request):
    items = Stock.objects.all()
    return render(request, "stock.html", {"stocks": items})


# store data to the Database

def fetch_and_store_data():
        # Insert data into the Stock model
        for stock in data:
             if isinstance(stock['marketCap'], str):
               stock['marketCap'] = int(stock['marketCap'].replace(',', ''))
        
             #insert Data into the stock model
             Stock.objects.update_or_create(
             symbol=stock['symbol'],
             defaults={
                  'companyName': stock['name'],
                  'marketCap': stock['marketCap'],
                  'url': stock['url']
             })


fetch_and_store_data()    