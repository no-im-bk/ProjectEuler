# build list of primes
import math
from bitarray import bitarray

# this is a guess for how far we need to search, but this made 78498 primes
n = 1000000

# construct a list of possible primes
composites = bitarray(n+1)
composites[0] = 1
composites[1] = 1

primes = []

# conduct a sieve for the primes
for x in range(2, n+1):
    if not composites[x]:
        for y in range(2*x,n + 1, x):
            composites[y] = 1
        primes.append(x)

print(primes[10000])