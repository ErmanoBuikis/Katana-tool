import random as rnd
from generate_strategy import *
from variables import *


def init_portfolio():
    laverage=rnd.choice(possible_laverage)
    portfolio={'buy_live':{'Capital':0},
                'sell_live':{},
                'laverage':laverage,
                'Capital':0}

    portfolio['buy_live'] = generate_strategy()
    portfolio['sell_live'] = generate_strategy() 
    portfolio['tick'] = {'tick_name':'EURUSD', 'n_ticks_used':n_ticks}
    
    return portfolio

