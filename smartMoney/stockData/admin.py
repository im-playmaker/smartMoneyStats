from django.contrib import admin
from .models import Stock, stockPrice

# Register your models here.
admin.site.register(Stock)
admin.site.register(stockPrice)