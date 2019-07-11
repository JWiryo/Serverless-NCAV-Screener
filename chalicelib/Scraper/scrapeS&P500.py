import pandas as pd
import json

from urllib.request import urlopen

def get_sp500_ticker_symbol_list():
    # Read Data from Wikipedia List of S&P500 Companies
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    # Get the list of tickerSymbols
    tickerTable = data[0]
    tickersList = tickerTable['Symbol'].tolist()

    # Call API to get balance sheet
    response = urlopen("https://financialmodelingprep.com/api/company/profile/AAPL?datatype=json")
    data = response.read().decode("utf-8")
    print(json.loads(data))

get_sp500_ticker_symbol_list()

