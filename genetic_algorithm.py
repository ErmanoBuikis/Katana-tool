import random as rnd

from math_equation import *
from variables import *
from normalization import *

def mutate_equations(bots):
    for i in range(len(bots)):
        for k,v in bots[i]['buy_live']['index'].items():
            if rnd.random() > mutation_rate:
                eq = equation()
                bots[i]['buy_live']['index'][k]['equation'] = sym.Add(eq,equation())
                bots[i]['buy_live']['index'][k]['normalization'] = choose_normalization()
    return bots

def select(bots):
    from copy import deepcopy
    idx = int(round(generation_size*rateo_survival))
    children = sorted(bots, key = lambda k: k['buy_live']['equity'],reverse=True) # sort 
    children = deepcopy(children[ :idx ])
    del(bots) 
    return children



def cross_over(bots):
    for i in range(int(round(generation_size*(1-rateo_survival)))):

        idx1 = rnd.choice(range(len(bots)))
        idx2 = rnd.choice(range(len(bots)))
        idx3 = rnd.choice(range(len(bots)))

        random_crossover = rnd.random()

        if random_crossover > 0.5:
            # mix strategy 3 parents
            c1 = bots[idx1]['buy_live']
            c2 = bots[idx1]['sell_live']
            c3 = bots[idx2]['buy_live']
            c4 = bots[idx2]['sell_live']
            c5 = bots[idx3]['buy_live']
            c6 = bots[idx3]['sell_live']

            random_mix = [ c1, c2, c3, c4, c5, c6]

            bots[idx1]['buy_live'] = rnd.choice(random_mix)
            bots[idx1]['sell_live'] = rnd.choice(random_mix)

            bots[idx2]['buy_live'] = rnd.choice(random_mix)
            bots[idx2]['sell_live'] = rnd.choice(random_mix)

            bots[idx3]['buy_live'] = rnd.choice(random_mix)
            bots[idx3]['sell_live'] = rnd.choice(random_mix)

        else:
            # swipe 2 equations
            keys1 = bots[idx1]['buy_live']['index'].keys()
            k1 = rnd.choice(list(keys1))
            eq1 = bots[idx1]['buy_live']['index'][k1]['equation'] 
            
            keys2 = bots[idx2]['buy_live']['index'].keys()
            k2 = rnd.choice(list(keys2))
            eq2 = bots[idx2]['buy_live']['index'][k2]['equation']

            bots[idx1]['buy_live']['index'][k1]['equation'] = eq2
            bots[idx2]['buy_live']['index'][k2]['equation'] = eq1

    return bots

