from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializers import ExchangeRateSerializer
from project.exchangerate.models import ExchangeRate
from rest_framework_api_key.permissions import HasAPIKey
from django.conf import settings
from .utils import parse_response

import requests


class ExchangeRateView(ListCreateAPIView):
    permission_classes = [HasAPIKey]
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()

    def post(self, request, *args, **kwargs):
        alphavantage_api_url = f"{settings.ALPHA_VANTAGE_API_BASE_URL}{settings.ALPHA_VANTAGE_API_QUERY_PARAMS}" \
                               f"&apikey={settings.ALPHA_VANTAGE_API_KEY}"
        response = requests.get(alphavantage_api_url)
        parsed_response = parse_response(response.text)
        serializer = self.get_serializer(data=parsed_response)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'exchange_rate': serializer.data})
