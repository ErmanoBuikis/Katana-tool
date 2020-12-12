#from check_sintax import *
from variables import *
import random as rnd


def choose_indexes_with_reintroduction(indexes_name_list):
    choosen=rnd.choice(indexes_name_list)
    return(choosen, indexes_name_list)

def generate_logic_rules():    
    
    trading_rules = '' #  [ opening_rules_op1 , closing_rules_op1, opening_rules_op2 , closing_rules_op2 ]
    
    financial_indexes = fin_idx # from variables
    
    index_number = rnd.randrange(min_index_number_allowed, max_index_number_allowed)
    
    operation_trading_rule= ''
    
    for i in range(index_number):

        idx, financial_indexes = choose_indexes_with_reintroduction(financial_indexes)  # index choosen
        
        #financial_indexes = financial_indexes.remove(idx) # possible bug trabscribing on fin_idx
        
        if operation_trading_rule: # starting
            br = R(3)

            operation_trading_rule += ' '+rnd.choice(logic_and_or)+br_open[br]+ idx+'_a '+ major_minor[R()]+ ' ' +idx+'_b '+ br_close[br]
        
        else:
            br = R(3)
            operation_trading_rule += ' '+br_open[br]+ idx + '_a '+ major_minor[R()]+ ' ' +idx+'_b '+br_close[br]+' '

    operation_trading_rule=check_empty_logic(operation_trading_rule)
    return operation_trading_rule

def check_empty_logic(trading_rule):
    while not trading_rule : # Avoid the blank trading rules
        try:
            trading_rule = generate_logic_rules()
        except:
            print(' generate_logic_rules - failed')

    open_brackets,close_brackets=0,0
    for i in trading_rule:
        if i =='(':
            open_brackets+=1
        if i==')':
            close_brackets+=1
    
    for i in trading_rule:
        if open_brackets > close_brackets:
            trading_rule=trading_rule+')'
            close_brackets+=1
        elif open_brackets<close_brackets:
            trading_rule='('+trading_rule
            open_brackets+=1
        else:
            continue

    return trading_rule

def generete_stats(): # TO FINISH
    max_capital_investment = round(rnd.uniform(0.01,0.5) , 3)
    max_number_operation_at_same_time = rnd.randint(1,100)
    possible_levarage = [1,10,20,50,100,200,500]
    levarage = rnd.choice(possible_levarage)
    return [levarage,max_capital_investment,max_number_operation_at_same_time]

def R(number_choice=2):
    """ randomize a choice for the generating rules """
    return(rnd.randrange(0,number_choice))

def check_logic(logic_rules_str):
    rules=logic_rules_str.replace('(',' ').replace(')',' ')
    rules=rules.replace('>',' ').replace('<',' ')
    for i in logic_and_or:
        rules=rules.replace(i,' ')
    return rules

