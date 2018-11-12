import time
import random

def timer( function ):
  def wrapper( *args, **kwargs):
    print( args, kwargs )
    start_ts = time.time()
    result = function( *args, **kwargs )
    end_ts = time.time()
    print( "Time of execution of function '{}' is {} ms." \
    .format( function.__name__, (end_ts-start_ts) * 1000 ) )
    return result
  return wrapper

def sleeper( from_, to_ ):
  def sleeper_( function ):
    def wrapper( *args, **kwargs ):
      time.sleep( random.randint( from_, to_ ) )
      print( "We gonna sleep {} seconds")
      result = function( *args, **kwargs )
      return result
    return wrapper
  return sleeper_



@timer
@sleeper( 1, 3 )
def foo( a, b ):
  time.sleep( 5)
  return a + b

if __name__=="__main__":
  print( foo(b=10, a=5) )
