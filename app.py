from chalice import Chalice

from chalicelib.scraper.scrapeSP500 import SP500Scraper
from chalicelib.calculator.calculateNCAV import NcavCalculator
from chalicelib.decider.stockDecider import StockDecider
from chalicelib.mailer.mailer import Mailer

app = Chalice(app_name='serverlessNCAVScreener')


@app.route('/')
def find_cheap_stocks():
    # Initialize Objects
    scraper = SP500Scraper()
    ncav_calculator = NcavCalculator()
    stock_decider = StockDecider()
    mailer = Mailer()

    good_ncav_shares_list = []
    email_content = ""

    # Scrape SP500 Tickers Data
    tickers_list = scraper.get_ticker_symbol_less_than_5()

    for ticker in tickers_list:

        # Calculate NCAV Value
        ncav_value = ncav_calculator.calculate_ncav(ticker)

        # If Positive, calculate NCAV Value
        if ncav_value >= 0:
            ncav_value_per_share = ncav_calculator.calculate_ncav_per_share(ticker, ncav_value)
            isCheap, price = stock_decider.decide_to_buy_stock(ticker, ncav_value_per_share)
            if isCheap:
                good_ncav_shares_list.append((ticker, price))
        else:
            continue

    for cheap_stock_tuple in good_ncav_shares_list:
        email_content += "%s %s \n" % (cheap_stock_tuple[0], cheap_stock_tuple[1])

    mailer.sendEmail(email_content)


find_cheap_stocks()
