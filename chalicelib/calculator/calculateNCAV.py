import json

from urllib.request import urlopen

def calculateNCAV():

    # Call API to get balance sheet
    url = "https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/AAPL?datatype=json"
    response = urlopen(url)
    decodedAPIData = response.read().decode("utf-8")

    # Get relevant financial data
    financialData = json.loads(decodedAPIData)['financials'][0]
    totalCurrentAssets = float(financialData['Total current assets'])
    totalLiabilities = float(financialData['Total liabilities'])

    # Calculate NCAV
    ncavValue = totalCurrentAssets - totalLiabilities
    return ncavValue

calculateNCAV()

