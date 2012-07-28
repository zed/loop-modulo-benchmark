"""Benchmark http://stackoverflow.com/questions/11641098/interpreting-a-benchmark-in-c-clojure-python-ruby-scala-and-others#comment15487214_11641098

Support for CPython 2.x, CPython 3, Jython, Pypy, RPython, Cython

from the same source.
"""
try:
    import cython
except ImportError: # provide dummy cython if it is not available
    class Cython:
        compiled = False
        def locals(*args, **kwargs):
            return lambda func: func
    cython = Cython()

##start_cython_hide
#NOTE: to generate fast loops `xrange` modification should be hidden from Cython
if not cython.compiled: #XXX doesn't help
    try:
        xrange = xrange
    except NameError: # Python 3 compatibility
        xrange = range
##end

@cython.locals(n=int,j=int)
def is_prime(n):
    for j in xrange(2, n):
        if n % j == 0:
            return False
    return True

def primes_below(x):
    return [(j-6, j) for j in xrange(9, x + 1) if is_prime(j) and is_prime(j-6)]

def main(argv):
    n = int(argv[1]) if len(argv) > 1 else 100*1000
    print(primes_below(n))
    return 0

def target(*args): # for RPython
    return main, None

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
