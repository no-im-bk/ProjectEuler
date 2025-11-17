# we need to find the prime factorization of each number <= 20
# and then take the union of the prime factorizations and then multiply the result

# build list of primes
import math
from bitarray import bitarray
n = 20

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

# now find the union of all prime factorizations of the numbers <= 20
primeFactorizationIntersection = {}
for x in range(2, n+1):
    primeFactorization = {}
    # find the prime factorization of the number
    for y in primes:
        while x % y == 0:
            x /= y
            primeFactorization[y] = primeFactorization.get(y, 0) + 1
    # now take the union of that number's prime factorization with the rest
    primeFactorizationIntersection = {y: max(primeFactorization.get(y, 0), primeFactorizationIntersection.get(y, 0)) for y in primeFactorization.keys() | primeFactorizationIntersection.keys()}

# multiply out the prime factorization
print(math.prod(x**primeFactorizationIntersection[x] for x in primeFactorizationIntersection))