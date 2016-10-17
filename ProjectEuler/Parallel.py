from joblib import Parallel, delayed
import multiprocessing
from multiprocessing import Process, Queue



def ParalelProcess(function, array):
    num_cores = multiprocessing.cpu_count()   
    results = Parallel(n_jobs=num_cores)(delayed(function)(i) for i in array)

    return results

