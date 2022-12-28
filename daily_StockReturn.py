#Daily Stock Return Project
#Dylan Smith
#Dec 27th 2022


#grabbing historical price data from a source
#source - use Yahoo Finance
#import all neccesary packages
import yfinance as yf
import pandas as pd
from tabulate import tabulate
from datetime import datetime
import matplotlib.pyplot as plt

companyTicker = 'V'
ticker = yf.Ticker(companyTicker)
historical = ticker.history(period = "3Y")

#initialize pandas data frame, also pull relevant data to task at hand and store in subset dataframe
historicalDF = pd.DataFrame(historical)
stockReturnData = historicalDF[['Close', 'Dividends']]

#using daily returns - this will allow us to calculate how many data points of daily data we have
numPeriods = len(stockReturnData['Close'])

#Create a column to keep track of the returns
stockReturnData.insert(2, 'Return',0.0,allow_duplicates = False)

#Calculate the daily returns for the ticker selected and data set pulled
for i in range(1,numPeriods):
    stockReturnData.iloc[i,2] = round( ((stockReturnData.iloc[i,0] - stockReturnData.iloc[i-1,0]) + stockReturnData.iloc[i,1] ) / (stockReturnData.iloc[i-1,0])  * 100 , 2)

#can change output to console to max to see full fancy output or export to csv/excel file.
print(tabulate(stockReturnData, headers = 'firstrow', tablefmt='fancy_grid'))

#for simplicity I have graphed this to see data
plt.plot(stockReturnData.index, stockReturnData.Return)
plt.title(companyTicker + " " + "Historical Daily Returns")
plt.xlabel("Date")
plt.ylabel('Return (%)')
plt.show()


