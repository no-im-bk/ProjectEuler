# build list of primes
import math
from bitarray import bitarray
n = 600851475143
sqrt_n = int(math.sqrt(n))

# construct a list of possible primes
primes = bitarray(sqrt_n+1)
primes[0] = 1
primes[1] = 1

ans = 0
# conduct a sieve for the primes
for x in range(2, sqrt_n+1):
    if not primes[x]:
        for y in range(2*x,sqrt_n + 1, x):
            primes[y] = 1
        # if we found a prime, also divide n by the prime
        while(n % x == 0):
            n /= x
            ans = x




print(ans)