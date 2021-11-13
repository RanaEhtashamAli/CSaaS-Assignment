from project.celery import app
from project.exchangerate.api.v1.serializers import ExchangeRateSerializer
from project.exchangerate.api.v1.utils import parse_response
from django.conf import settings

import requests

@app.task
def get_latest_exchange_rate():
    alphavantage_api_url = f"{settings.ALPHA_VANTAGE_API_BASE_URL}{settings.ALPHA_VANTAGE_API_QUERY_PARAMS}" \
                           f"&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    response = requests.get(alphavantage_api_url)
    parsed_response = parse_response(response.text)
    serializer = ExchangeRateSerializer(data=parsed_response)
    serializer.is_valid(raise_exception=True)
    serializer.save()

