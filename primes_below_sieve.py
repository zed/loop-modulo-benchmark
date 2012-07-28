# Interpreting a benchmark in C, Clojure, Python, Ruby, Scala and others
"""Better algorithm for http://stackoverflow.com/q/11641098"""
# http://stackoverflow.com/questions/11641098/interpreting-a-benchmark-in-c-clojure-python-ruby-scala-and-others
try:
    xrange = xrange
except NameError: # python 3 compatibility
    xrange = range


def primes_below(limit): # Sieve of Eratosthenes
    prime = [True]*limit
    for n in xrange(2, limit): #NOTE: not including limit
        if prime[n]:
            for k in xrange(n*n, limit, n):
                prime[k] = False # mark composites

            if n > 7 and prime[n-6]:
                yield (n-6), n

correct100 = [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29),
        (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73),
        (73, 79), (83, 89)]
assert list(primes_below(100)) == correct100


from timeit import default_timer as timer

def benchmark():
    start = timer()
    #NOTE: print(list()) inside
    print(list(primes_below(100*1000)))
    print("%.2f seconds" % (timer()-start,))

benchmark()

