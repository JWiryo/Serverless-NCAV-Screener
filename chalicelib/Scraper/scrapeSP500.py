import pandas as pd
import json

from urllib.request import urlopen


class SP500Scraper:

    @staticmethod
    def get_sp500_ticker_symbol_list():
        # Read Data from Wikipedia List of S&P500 Companies
        data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

        # Get the list of tickerSymbols
        ticker_table = data[0]
        tickers_list = ticker_table['Symbol'].tolist()

        return tickers_list

    @staticmethod
    def get_ticker_symbol_less_than_5():
        # Initiate Very Cheap Stocks List
        very_cheap_stocks_list = []

        # Call API to get ticker symbols less than $5
        stock_symbols_url = 'https://financialmodelingprep.com/api/v3/company/stock/list'
        symbols_response = urlopen(stock_symbols_url)
        decoded_symbols_response = symbols_response.read().decode("utf-8")

        symbols_list = (json.loads(decoded_symbols_response)["symbolsList"])
        for symbol in symbols_list:
            if float(symbol["price"]) <= 5:
                very_cheap_stocks_list.append(symbol["symbol"])

        return very_cheap_stocks_list
