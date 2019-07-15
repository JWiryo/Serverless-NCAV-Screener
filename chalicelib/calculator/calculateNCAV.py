import json

from urllib.request import urlopen

def calculateNCAVPerShare():

    # Call API to get balance sheet
    balanceSheetUrl = "https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/AAPL?period=quarter?datatype=json"
    balanceSheetResponse = urlopen(balanceSheetUrl)
    decodedBalanceSheetData = balanceSheetResponse.read().decode("utf-8")

    # Get relevant balance sheet data
    balanceSheetData = json.loads(decodedBalanceSheetData)['financials'][0]
    totalCurrentAssets = float(balanceSheetData['Total current assets'])
    totalLiabilities = float(balanceSheetData['Total liabilities'])

    # Call API to get income statement
    incomeStatementUrl = "https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL?period=quarter?datatype=json"
    incomeStatementResponse = urlopen(incomeStatementUrl)
    decodedIncomeStatementData = incomeStatementResponse.read().decode("utf-8")

    # Get relevant income statement data
    incomeStatementData = json.loads(decodedIncomeStatementData)['financials'][0]
    totalSharesOutstanding = float(incomeStatementData['Weighted Average Shs Out'])

    # Calculate NCAV/share
    ncavValue = totalCurrentAssets - totalLiabilities
    ncavValuePerShare = ncavValue / totalSharesOutstanding
    return ncavValuePerShare

calculateNCAVPerShare()

