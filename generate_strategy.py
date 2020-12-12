import pandas as pd
import numpy as np
import random as rnd

from logic import *
from math_equation import *
from normalization import *



def generate_strategy():
    dict_equation = {}

    logic_str = generate_logic_rules()
    list_logic_elements=check_logic(logic_str)
    list_logic_elements = extract_list_logic_elements(list_logic_elements)
    
    dict_equation['index']={}

    for i in range(len(list_logic_elements)) :
        dict_equation['index'][list_logic_elements[i]] = {'equation':equation(),
                                                         'normalization':choose_normalization()}
    
    dict_equation=TakeProfitStopLoss(dict_equation)
    dict_equation['Logic']=logic_str
    return(dict_equation)

def TakeProfitStopLoss(dict_equation):
    dict_equation['TP'] = round(rnd.uniform(0.001,0.01),8)
    dict_equation['SL'] = round(rnd.uniform(0.001,0.01),8)
    return dict_equation

def extract_list_logic_elements(sting_logic_equation):
    """{' ( cci_a< cci_b)': sin(x) ==> 'cci_a': sin(x)  """
    list_elements = sting_logic_equation.split() 
    return [i for i in list_elements]

def prepare_logic_string(name_df, strategy):
    string_logic = strategy['Logic']
    for i in strategy['index'].keys():
        if i in string_logic:
            string_logic=string_logic.replace(i,name_df+"."+i+" ")
    string_logic=string_logic.replace("and"," & ").replace("or"," | ").replace("edf","df")
    return string_logic