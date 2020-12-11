#!/usr/bin/python3
#!coding=utf-8

# NORMALIZATION METHODS

import math

import numpy as np
import pandas as pd


from numba import jit
import random as rnd
from variables import available_normalizations


def choose_normalization():
    """select random normalization"""
    # input dictionary = available_equations
    return available_normalizations[rnd.randint(0,len(available_normalizations)-1)]

def apply_normalization(normalization_method,nparray):
    # must be applied to arrays
    # and not direct to equation
    n_type = normalization_method
    if n_type=='n1':
        return n1(nparray)
    elif n_type=='n2':
        return n2(nparray)
    elif n_type=='n3':
        return n3(nparray)
    elif n_type=='n4':
        return n4(nparray)
    elif n_type=='n5':
        return n5(nparray)
    elif n_type=='n6':
        return n6(nparray)
    elif n_type=='n7':
        return n7(nparray)  
    else:
        print(' normalization type error')

#@jit(nopython=True)
def n1(nparray):
    """ ( array - Min) / (Max - Min) """
    return (nparray - np.min(nparray)) / (np.max(nparray) - np.min(nparray))
    
#@jit(nopython=True)
def n2(nparray):
    """(array - mean) / sd """
    return (nparray - np.mean(nparray) ) / np.std(nparray)

#@jit(nopython=True)
def n3(nparray):
    """(array - mean) / var """
    return (nparray - np.mean(nparray) ) / np.var(nparray)

#@jit(nopython=True)
def n4(nparray):
    """(array - mean) / (Max - min) """
    return (nparray - np.mean(nparray)) / (np.max(nparray) - np.min(nparray))

#@jit(nopython=True)
def n5(nparray):
    """ 1 / (1 + e^(-i)) """
    e = 2.71828
    return 1 / (1 + e**(-nparray))

#@jit(nopython=True)
def n6(nparray):
    """ log(i) / (1 - log(i) ) """
    return np.log10(np.absolute(nparray)) / (1 - np.log10(np.absolute(nparray)))

#@jit(nopython=True)
def n7(nparray):
    var = rnd.random()
    return 1 / (1 + (1+var)**(-nparray))