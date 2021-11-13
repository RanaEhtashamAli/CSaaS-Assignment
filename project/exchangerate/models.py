from django.db import models

# Create your models here.

class ExchangeRate(models.Model):
    from_currency_code = models.CharField(max_length=3)
    from_currency_name = models.CharField(max_length=50)
    to_currency_code = models.CharField(max_length=3)
    to_currency_name = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=17, decimal_places=8)
    last_refreshed = models.DateTimeField()
    time_zone = models.CharField(max_length=3)
    bid_price = models.DecimalField(max_digits=17, decimal_places=8)
    ask_price = models.DecimalField(max_digits=17, decimal_places=8)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
