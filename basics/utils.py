import math
import random
from functools import wraps 
from time import time

def an_int(within=None):
    if within is None:
        within = [-5000, + 5000]
    return random.randint(within[0], within[1])


def array_of_random_ints(size, within=None, duplicates=0):
    if within is None:
        within = [-5000, + 5000]

    ints = [random.randint(within[0], within[1]) for x in range(size)]
    if duplicates > 0:
        a = random.randint(0, size-1)
        b = random.randint(0, size-1)
        ints[b] = ints[a]

    return ints

# print(array_of_random_ints(5, [1, 100], duplicates=2))

avg_times = {}

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func: %r took %2.4f sec' % (f.__name__, te-ts))
        if f.__name__ in avg_times:
            rec = avg_times[f.__name__]
            rec[1] = (rec[1] + te-ts)/rec[0]
            rec[0] += 1
        else:
            avg_times[f.__name__] = [1, te-ts]
            
        return result

    return wrap

def print_timings():
    for k, v in avg_times.items():
        print(k, "%2.4f" % v[1])
