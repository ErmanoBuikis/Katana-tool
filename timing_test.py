from functools import wraps
from time import time

def timing(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print (' - {0} \t| time: {1} | Type output: {2}'.format(str(f).split()[1],round(end-start,3),str(type(result)).split()[1]))
        return result
    return wrapper