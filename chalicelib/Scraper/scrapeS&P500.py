import pandas as pd


def get_sp500_ticker_symbol_list():
    # Read Data from Wikipedia List of S&P500 Companies
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    # Get the list of tickerSymbols
    ticker_table = data[0]
    tickers_list = ticker_table['Symbol'].tolist()

    return tickers_list
