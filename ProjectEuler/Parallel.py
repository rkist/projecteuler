from distributed import joblib
from joblib import Parallel, delayed

import multiprocessing
from multiprocessing import Process, Queue



def ParallelProcess(function, array, num_cores = 0):
    if (num_cores == 0):
        num_cores = multiprocessing.cpu_count()
    results = Parallel(n_jobs=num_cores)(delayed(function)(i) for i in array)

    return results


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]        

    return memoized_func
