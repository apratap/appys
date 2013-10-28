#!/usr/bin/env python



import os
import sys
import multiprocessing



#decorator to run a function in parallel
#deocorator accepts an argument as number of cores
#run a func in parallel
'''
def parallelize_decorator(N):                      
    def wrapper_to_accept_func_to_be_decorated(func):        
        def wrapped(values):
            from multiprocessing import Pool, cpu_count
            num_cores = N #create a local copy can't modify a closure arg
            if num_cores is None:
                num_cores = cpu_count() - 1 if cpu_count() > 2 else 1
            print'Using %d cores' % num_cores
            pool = Pool(num_cores)
            try:
                print values
                #result = pool.map(func, values)
                pool.close()
            except KeyboardInterrupt:
                print 'got ^C while pool mapping, terminating the pool'
                pool.terminate()
                print 'pool is terminated'
            except Exception, e:
                print 'got exception: %r, terminating the pool' % (e,)
                p.terminate()
                print 'pool is terminated'
            finally:
                pool.join()
            #return result    
        return wrapped
    return wrapper_to_accept_func_to_be_decorated

'''


def parallelize_func_singe_input(func,input_list,num_cores=None):
    from multiprocessing import Pool, cpu_count
    if num_cores is None:
        num_cores = cpu_count() - 1 if cpu_count() > 2 else 1
    if num_cores > cpu_count():
        num_cores = cpu_count() 
    print'Using %d cores' % num_cores
    pool = Pool(num_cores)
    try:
        result = pool.map(func,input_list)
        pool.close()
    except KeyboardInterrupt:
        print 'got ^C while pool mapping, terminating the pool'
        pool.terminate()
        print 'pool is terminated'
    except Exception, e:
        print 'got exception: %r, terminating the pool' % (e,)
        p.terminate()
        print 'pool is terminated'
    finally:
        pool.join()
    return result    


