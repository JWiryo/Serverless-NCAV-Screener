import json

from urllib.request import urlopen


class NcavCalculator:

    @staticmethod
    def calculate_ncav(ticker):
        # Call API to get balance sheet
        balance_sheet_url = 'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{}?period=quarter?datatype=json'.format(ticker)
        balance_sheet_response = urlopen(balance_sheet_url)
        decoded_balance_sheet_data = balance_sheet_response.read().decode("utf-8")

        # Get relevant balance sheet data
        if json.loads(decoded_balance_sheet_data)['financials']:
            balance_sheet_data = json.loads(decoded_balance_sheet_data)['financials'][0]

            if balance_sheet_data['Total current assets'] != '':
                total_current_assets = float(balance_sheet_data['Total current assets'])
            else:
                total_current_assets = 0
            if balance_sheet_data['Total liabilities'] != '':
                total_liabilities = float(balance_sheet_data['Total liabilities'])
            else:
                total_liabilities = 0

            ncav_value = total_current_assets - total_liabilities
            return ncav_value
        else:
            return 0

    @staticmethod
    def calculate_ncav_per_share(ticker, ncav_value):
        # Call API to get income statement
        income_statement_url = "https://financialmodelingprep.com/api/v3/financials/income-statement/{}?period=quarter?datatype=json".format(ticker)
        income_statement_response = urlopen(income_statement_url)
        decoded_income_statement_data = income_statement_response.read().decode("utf-8")

        # Get relevant income statement data
        if json.loads(decoded_income_statement_data)['financials']:
            income_statement_data = json.loads(decoded_income_statement_data)['financials'][0]
            total_shares_outstanding = float(income_statement_data['Weighted Average Shs Out'])

            # Calculate NCAV/share
            ncav_value_per_share = ncav_value / total_shares_outstanding
            return ncav_value_per_share
        else:
            return 0
