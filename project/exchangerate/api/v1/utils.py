import json


def parse_response(response):
    json_response = json.loads(response)
    if "Realtime Currency Exchange Rate" in json_response:
        json_response = json_response['Realtime Currency Exchange Rate']
        parsed_response = {
            "from_currency_code": json_response.get('1. From_Currency Code'),
            "from_currency_name": json_response.get('2. From_Currency Name'),
            "to_currency_code": json_response.get('3. To_Currency Code'),
            "to_currency_name": json_response.get('4. To_Currency Name'),
            "exchange_rate": json_response.get('5. Exchange Rate'),
            "last_refreshed": json_response.get('6. Last Refreshed'),
            "time_zone": json_response.get('7. Time Zone'),
            "bid_price": json_response.get('8. Bid Price'),
            "ask_price": json_response.get('9. Ask Price'),
        }
        return parsed_response

