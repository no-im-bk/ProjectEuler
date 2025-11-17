# build list of primes
import math
from bitarray import bitarray
n = 2000000

# construct a list of possible primes
composites = bitarray(n+1)
composites[0] = 1
composites[1] = 1

ans = 0
# conduct a sieve for the primes
for x in range(2, n+1):
    if not composites[x]:
        for y in range(2*x, n + 1, x):
            composites[y] = 1
        # if we found a prime, also divide n by the prime
        ans += x

print(ans)