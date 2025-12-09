from bitarray import bitarray


print("First get our list of primes less than 10000000")
primeList = []
n = 10000000

composites = bitarray(n)
composites[0] = 1
composites[1] = 1

for x in range(2, n):
    if composites[x]:
        pass
    else:
        primeList.append(x)
        for i in range(2*x, n, x):
            composites[i] = 1


print("Now I'll define a function for finding the number of divisors")
def numDivisors(x) -> int:
    count = 1
    for prime in primeList:
        powerOfFactor = 0
        while x % prime == 0:
            powerOfFactor += 1
            x //= prime
        count *= powerOfFactor + 1
        if x == 1:
            return 1 + count
    return 1 + count
        

print("Now keep trying triangular numbers till we find the one with > 500 divisors")
for x in (n * (n + 1) // 2 for n in range(1,100000000)):
    if numDivisors(x) > 500:
        print(x)
        break
