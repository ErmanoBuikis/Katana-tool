"""
Ermano Buikis

Trading Algorithm Tool for backtesting and generating equation

https://github.com/ErmanoBuikis/Katana-tool/tree/master

"""
# __________External libraries__________
import os
import sys

import random as rnd
from pprint import pprint
import configparser 
from copy import deepcopy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sympy import *
from sympy.abc import x

import multiprocessing as mp
import time
from timing_test import timing

# __________ Project modules__________
from variables import *

from finance_indexes import CCI,RSI,ROC,SMA,SMI,MACD,EMA,SMA_numba

from load_data import eurusd, apachecorp_data
from load_data import BTCUSD_data, ETHUSD_data, ZECUSD_data

from logic import *
from math_equation import *
from normalization import *

    
from init_portfolio import init_portfolio  

from generate_strategy import *
from buy_live_strategy import buy_live_strategy

from genetic_algorithm import mutate_equations,cross_over,select




def fix_empty_structure(bots_):
    "fix possible empty structure"
    for n_bot in range(len(bots_)): 
        if  'equity' not in bots_[n_bot]['buy_live'].keys():
            bots_[n_bot]['buy_live']['equity'] = initial_capital
    return bots_

def load_dataset():
    data = eurusd()
    #data = apachecorp_data()
    #data = BTCUSD_data()
    return data

#@timing
def main():
    
    n_bots=0
    bots=[]
    BEST = 0
    BEST_OBJ = {'buy_live':{'equity':0}}
    capitals=[]

    data = load_dataset()

    print(data.head())

    prices = data['Close'].to_numpy()
    prices = prices[-n_ticks + buffer_period:]

    ema = EMA(prices)
    sma = SMA(prices)
    sma_numba = SMA_numba(prices)
    rsi = RSI(prices)
    macd = MACD(prices)
    cci = CCI(data['High'].to_numpy(),
            data['Low'].to_numpy(),
            data['Close'].to_numpy())



    print('-'*10, ' Generation Zero ' ,'-'*10,'\n\n ')
    for i in range(generation_size):

        laverage=rnd.choice(possible_laverage)
        portfolio={'buy_live':{'equity':0},
                    'sell_live':{},
                    'laverage':laverage,
                    'Capital':0 }

        portfolio['buy_live'] = generate_strategy()
        portfolio['sell_live'] = generate_strategy() 
        portfolio['tick'] = {'tick_name':'EURUSD', 'n_ticks_used':n_ticks}

        portfolio = buy_live_strategy(prices,portfolio)
        bots.append(portfolio)


        if print_porfolio==True: print(portfolio)
        
        n_bots+=1

    bots = fix_empty_structure(bots)  

    bots = sorted(bots, key=lambda k: k['buy_live']['equity'],reverse=True)
    children = select(bots) # Genetic Algorithm - Select
    

    for n_gen in range(number_generations):
        
        print('\n','~'*10, ' n generation  : ',n_gen+1,'~'*10,'\n')

        while len(bots) < generation_size:
            # repopulate
            rnd_repop = rnd.random()
            if rnd_repop < 0.5: 
                portfolio = init_portfolio()
                portfolio = buy_live_strategy(prices,portfolio) # strategy


            elif rnd_repop >= 0.5 and rnd_repop < 0.6 : # 10%
                # repop from best actual population
                portfolio = rnd.choice(bots[:int(round(len(bots)*rateo_survival))])

                portfolio = buy_live_strategy(prices,portfolio) # strategy
                bots.append(portfolio) 


            else: # 80%
                # repop from children
                portfolio = rnd.choice(children)
                
                portfolio = buy_live_strategy(prices,portfolio) # strategy
                bots.append(portfolio) 

            if 'equity' in portfolio['buy_live'].keys():
                while ( portfolio['buy_live']['equity'] == -2 or 
                    portfolio['buy_live']['equity']==initial_capital):

                    portfolio = init_portfolio()
                    portfolio = buy_live_strategy(prices,portfolio)
                    bots.append(portfolio) 
            
            for n_bot in range(len(bots)):
                if 'equity' in bots[-1]['buy_live'].keys():
                    if BEST_OBJ['buy_live']['equity'] > bots[-1]['buy_live']['equity']:
                        BEST_OBJ = deepcopy(bots[n_bot])

            bots = fix_empty_structure(bots)  

            print(bots[-1]['buy_live']['equity']) 
        
        # Genetic Algorithm
        bots = sorted(deepcopy(bots), key=lambda k: k['buy_live']['equity'],reverse=True) # SELECT
        bots = deepcopy(bots[:round(len(bots)*rateo_survival)])
        bots = cross_over(deepcopy(bots))       # CROSS OVER
        children = mutate_equations(deepcopy(bots)) # MUTATE
        
           
    pprint(BEST_OBJ)



if __name__=="__main__":
    main()
