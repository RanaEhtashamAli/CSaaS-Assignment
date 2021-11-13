from django.contrib import admin
from .models import ExchangeRate


@admin.register(ExchangeRate)
class ExchnageRateAdmin(admin.ModelAdmin):
    list_filter = ['from_currency_code', 'to_currency_code']
    list_display = ['from_currency_code', 'to_currency_code', 'exchange_rate', 'last_refreshed']
