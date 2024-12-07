from django.db import models

# Create your models here.

# define a model for stock
class Stock (models.Model):
    symbol= models.CharField(max_length=10, unique=True) # Stock symbol (e.g., AAPL, TSLA)
    companyName =  models.CharField(max_length=100)  # Name of the company
    marketCap =  models.BigIntegerField(default=0)  # Name of the company
    url =  models.URLField(default="https://example.com/default")  # Name of the company
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on object creation

    def __str__(self):
        return self.symbol

# Define stock price
class stockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='prices')  # Link to Stock model
    date = models.DateField()  # Date of the price record
    open_price = models.DecimalField(max_digits=10, decimal_places=2)  # Opening price
    close_price = models.DecimalField(max_digits=10, decimal_places=2)  # Closing price
    high_price = models.DecimalField(max_digits=10, decimal_places=2)  # Highest price
    low_price = models.DecimalField(max_digits=10, decimal_places=2)  # Lowest price
    volume = models.BigIntegerField()  # Volume of stocks traded


    class Meta:
        # Index on the date for faster query performance
        indexes = [
            models.Index(fields=['date']),
        ]
        ordering = ['date']
    
    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"

