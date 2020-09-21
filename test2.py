import pandas as pd 
import numpy as np
import requests
import csv

class DataGrab:
    def getBinanceSpot (self):
        """ Returns Data Frame with ask, bid, price, volume, base, quote, spread, exchange"""
        
        def splitPair(tickerString) :
            if tickerString[-4:] =='USDT':
                return [tickerString.split('USDT')[0].lower(),'usdt']
            
            elif tickerString[-3:] =='ETH':
                return [tickerString.split('ETH')[0].lower(),'eth']

            elif tickerString[-3:] =='BTC':
                return [tickerString.split('BTC')[0].lower(),'btc']

            elif tickerString[-3:] =='BNB':
                return [tickerString.split('BNB')[0].lower(),'bnb']
            
            return np.nan   

url = 'https://api.binance.com/api/v1/ticker/24hr'
bnn_df = pd.DataFrame(requests.get(url).json())
print (bnn_df)

a = DataGrab().getBinanceSpot()
print(a.to_csv('myBinanceData.csv'))
