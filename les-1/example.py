import sys
import math

import cProfile

def profiler( func ):
    def wrapper( *args, **kwargs):
        profile_filename = "{}.prof".format( func.__name__)
        profiler = cProfile.Profile()
        result = profiler.runcall( func, *args, **kwargs )
        profiler.dump_stats( profile_filename)
        return result
    return wrapper

@profiler
def is_prime( number ):
    for i in range(2, int( math.sqrt( number ) ) + 1 ):
        if number % i == 0:
            return False
    return True   

@profiler
def get_prime_numbers( number ):
    prime_numbers = [1]
    for num in range(2, number):
        if is_prime(num):
            prime_numbers.append( num )
    return prime_numbers


if __name__=="__main__":
    if len(sys.argv) != 2:
        print( "Usage: {} <number>".format( sys.argv[0] ) )
        sys.exit(1) #'echo $?' returns '1'
    number = int ( sys.argv[1] )
    prime_numbers = get_prime_numbers( number )
    print( len( prime_numbers ) )
