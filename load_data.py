from timing_test import timing

import sys
import pandas as pd

# FOREX
@ timing
def eurusd():
    path_price = str(sys.path[0]) + "/data/EUR_USD.txt" # specific file
    data_prices = pd.read_csv(path_price, sep =',') # load data
    data_prices.columns = ["Ticker","Date","Time","Open","High","Low","Close","Vol"] # set columns name
    data_prices = data_prices.drop(["Ticker"], axis=1) # drop columns

    return data_prices

# STOCK    
@ timing
def apachecorp_data():
    path_price = str(sys.path[0]) + "/data/apache_corp_daily.txt" # specific file
    data_prices = pd.read_csv(path_price, sep =',') # load data
    data_prices.columns = ["Date","Time","Open","High","Low","Close","Vol"] # set columns name
    return data_prices

# CRYPTO       
def ETHUSD_data(): # 367220 n_ticks
    path_price = str(sys.path[0]) + "/data/gemini_ETHUSD_2020_1min.csv" # specific file
    data_prices = pd.read_csv(path_price, sep =',') # load data
    data_prices = data_prices.drop(["Unix","Date","Symbol"], axis=1) # drop columns
    return data_prices

def BTCUSD_data(): # 367220 n_ticks
    path_price = str(sys.path[0]) + "/data/gemini_BTCUSD_2020_1min.csv" # specific file
    data_prices = pd.read_csv(path_price, sep =',') # load data
    data_prices = data_prices.drop(["Unix","Date","Symbol"], axis=1) # drop columns
    return data_prices   

def ZECUSD_data(): # 367220 n_ticks
    path_price = str(sys.path[0]) + "/data/gemini_ZECUSD_2020_1min.csv" # specific file
    data_prices = pd.read_csv(path_price, sep =',') # load data
    data_prices = data_prices.drop(["Unix","Date","Symbol"], axis=1) # drop columns
    return data_prices 