#!/usr/bin/python3
#!coding=utf-8

# type(equation) ==  <class 'sympy.core.add.Add'>
from timing_test import timing

import time
import random as rnd
import math
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

import pandas as pd
import sympy as sym  
from sympy.abc import x
from sympy import *
from variables import *

def equation():
    eq=generate_random_equation()
    while check_empty_logic(eq)==False: # check 0 equation
        eq=generate_random_equation()
    while check_zero_equation(eq)==False:
        eq=generate_random_equation()

    return eq

def choose_equation():
    """select random equation"""
    # input dictionary = available_equations
    return available_equations[rnd.randint(0,len(available_equations)-1)]

def generate_random_equation():
    eq_type=choose_equation()
    if eq_type=='polynomial':
        return polynomial()
    elif eq_type=='fourier':
        return fourier()
    elif eq_type=='mod_fourier':
        return mod_fourier()    
    else:
        print(' equation type error')


def polynomial():
    indexes_list = rnd.sample(range(max_grade_polynomial),
    rnd.choice(range(n_elemets_in_equation_poly)))  # pop , sample

    parameters_list = [rnd.choice(np.linspace(min_parameter_poly, max_parameter_poly)) for i in
                       range(len(indexes_list))]  # could be 0
    x = sym.Symbol('x')
    equation = sum(k * x ** i for k, i in zip(parameters_list, indexes_list))
    return equation

def fourier():
    indexes_list = rnd.sample(range(max_grade_fourier), rnd.choice(range(n_elemets_in_equation_fourier)))
    list_parameters_1 = np.random.randint(1,10,size=len(indexes_list))
    list_parameters_2 = np.random.randint(1,10,size=len(indexes_list))
    x = sym.Symbol('x')
    equation = sum(k * sym.sin(x) ** i - j * sym.cos(x) ** i for j, k, i in
                           zip(list_parameters_1, list_parameters_2,indexes_list))
    if type(equation) is not int :
        equation = equation.simplify()
    return equation

def mod_fourier():
    indexes_list = rnd.sample(range(max_grade_mod_fourier),rnd.choice(range(n_elemets_in_equation_mod_fourier))) 
    list_parameters_1 = np.random.randint(1,10,size=len(indexes_list)) # min, max, size
    list_parameters_2 = np.random.randint(1,10,size=len(indexes_list))
    x = sym.Symbol('x')
    equation = sum(k * sym.sin(x) ** i - j * sym.cos(x) ** i for j, k, i in
                           zip(list_parameters_1, list_parameters_2,indexes_list))
    if type(equation) is not int :
        equation = equation.simplify()                    
    return equation


def check_zero_equation(equation):
    if equation == 0:
        return False
    else:
        return True

def check_empty_logic(equation):
    equation_str=str(equation)
    if equation_str in not_valid_eq:
        return False
    else:
        return True

def idx_is_configured(indx_name, configured_idxs):
    if indx_name.lower() in configured_idxs:
        return True
    else:
        return False
