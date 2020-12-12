import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import seaborn as sns

from generate_strategy import *
from init_portfolio import init_portfolio

from variables import *

def format_time_stamp(time):
    " time = ticks in minutes"
    day = time // (24 * 60)
    time = time % (24 *60)
    hour = time // 60
    time %= 60
    minutes = time 
    return [day,hour,minutes]

#@timing
def buy_live_strategy(prices,portfolio):
    """ 
        buy live Strategy
        1 operation at time
        buy at the market
        leverage = ON
        Buy/LONG = ON
        Sell/SHORT = OFFs
     
    """


    if 'laverage' in portfolio:
        laverage = portfolio['laverage']
    else:
        portfolio = init_portfolio()

    capital = initial_capital

    df = pd.DataFrame()
    last_operation = 0

    try: 
        portfolio['buy_live']['equity']=initial_capital

        for financial_index, var in portfolio['buy_live']['index'].items():
            f = lambdify(x, var['equation'] ,"numpy") # symbol, expression, method computation
            data = f(prices)
            normalized_data = eval('{0}(data)'.format(var['normalization'])) # for both indexes (_a and _b)
            df[str(financial_index)] = normalized_data # add financial index to dataframe for test

        signal_string_strategy = prepare_logic_string('df',portfolio['buy_live']) # prepare eval string
        capital_through_time = [capital]
        
        # BOTTLE NECK
        df_bool = eval(signal_string_strategy) # evaluation of signal with boolean values 
        
        if (df_bool.any()==True):            
            open_signal=False

            for i in range(len(prices)):
                if df_bool[i]==True and open_signal==False:
                    open_price = prices[i] # Open position
                    open_signal=True

                if open_signal==True: # Check for close
                    gain = (prices[i]-open_price)*capital*laverage      
                    TP = portfolio['buy_live']['TP']*capital*laverage
                    SL = portfolio['buy_live']['SL']*capital*laverage
                    
                    if (gain  > TP or gain < -SL): # Close position 
                        capital += gain
                        portfolio['buy_live']['equity'] = capital
                        open_signal=False
                        

                        if print_operation == True:
                            date = format_time_stamp(last_operation)
                            print(round(capital,2),
                            ' TP|SL :',round(gain,2),
                            ' \t last op : d {0}-{1}:{2}'.format(date[0],date[1],date[2]),
                            ' \t process ',int((i/len(prices))*100),'% ')
                        last_operation = 0

                last_operation += 1
                capital_through_time.append(capital)
                #variance_pop = np.std(capital_through_time) # standard deviation population             
                
                if capital <= (1-max_drawdown)*initial_capital:
                    return portfolio

            if (print_plot_capital == True and len(capital_through_time)>1
                and capital > initial_capital ): 

                plt.plot(range(len(capital_through_time)), capital_through_time , color='red')
    
                Title = ('EURUSD | laverage '+str(portfolio['laverage'])+
                '\n Days: '+str(int(n_ticks/(60*24)))+
                '\n Years '+str(round(n_ticks/(60*24*365)))+
                '\n gain '+str(round((capital-initial_capital)/initial_capital*100,2))+' %')
                
                plt.title(label=Title)
    
                plt.ylabel(' Equity ')
                plt.show()
        
        return portfolio


    except:
        portfolio['buy_live']['equity'] = -2
        return portfolio

# 