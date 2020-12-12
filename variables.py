#!/usr/bin/python3
#!coding=utf-8

# PRINT
print_operation = True # gain for each operation
print_plot_capital = True # capital through time plot
print_porfolio = False # data structure 

data_configured = ['EURUSD']

n_ticks = 6_500_000  
    # eurusd |  6_500_000 
    # crypto |  367_220
buffer_period = 200 # start from here

# GENETIC ALGORITHM
number_generations = 5
generation_size = 30 # number of bots in the same generation

mutation_rate = 0.8  
rateo_survival = 0.5 


# FINANCE
initial_capital = 10_000

possible_laverage = [1,2,3,4,5]
max_drawdown = 0.5      # 0.5 = 50%

# Variables Finance configured
fin_idx = ['rsi', 'macd' ,'ema','ma','cci','atr','smi','roc']  
oscillators =[ 'macd' , 'atr' ] 

# building strategy elements
logic_and_or = ['and' , 'or']
math_symbols = ['/' , '*' , '+' , '-' , '**' , 'log' , 'ln']
major_minor = ['>' , '<']
br_open = ['(' , ' ','((']
br_close = [')' , ' ','))']
not_valid_eq = [' ','','(( )','( ))','(())','()']


# MATH
n_methods_normalization = 6 # number of method for normalization

max_index_number_allowed = 4 # max number of finance indexes in single equation
min_index_number_allowed = 1 # min number of finance indexes in single equation

max_operations_at_same_time = 1 # number of max operations at the same time allowed
max_percentage_of_investment = 5 # max %invest of the capital on Take Profit or Stop Loss (MAX 5%)

# polynomial
max_grade_polynomial = 8 # max grade of the polinomial
n_elemets_in_equation_poly = 5 # max number of elements allowed in the same function
min_parameter_poly = -100 # min of the parameters of the equation
max_parameter_poly = 100 # max of the parameters of the equation

# fourier
max_grade_fourier = 8  # max grade of the fourier
n_elemets_in_equation_fourier = 5
min_parameter_fourier = -100
max_parameter_fourier = 100

# modded fourier
max_grade_mod_fourier = 8
n_elemets_in_equation_mod_fourier = 5
min_parameter_mod_fourier = -100
max_parameter_mod_fourier = 100

not_valid_eq = [' ','','(( )','( ))','(())','()']

available_equations = { 0:'polynomial',
                        1:'fourier',
                        2:'mod_fourier'
                      }

available_normalizations = { 0 : 'n1',
                            1 : 'n2',
                            2 : 'n3',
                            3 : 'n4',
                            4 : 'n5',
                            5 : 'n6',
                            6 : 'n7'
                            }