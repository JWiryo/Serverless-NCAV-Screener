import json

from urllib.request import urlopen
from chalicelib.constants import BUY_THRESHOLD


class StockDecider:

    @staticmethod
    def decide_to_buy_stock(ticker, ncav_value_per_share):

        # Call API to get current price
        realtime_price_url = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}?datatype=json'.format(
            ticker)
        realtime_price_response = urlopen(realtime_price_url)
        decoded_realtime_price_data = realtime_price_response.read().decode("utf-8")

        # Get latest price data
        current_price = float(json.loads(decoded_realtime_price_data)['price'])

        # Decide if price is below buy threshold
        if current_price <= BUY_THRESHOLD * ncav_value_per_share:
            return True, current_price
        else:
            return False, ncav_value_per_share
