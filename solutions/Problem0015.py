# We have 20 options to turn left or right, and 10 have to be left.
# Thus we find 20C1-
from math import factorial
n = 20
print(factorial(2 * n) // (factorial(n)*factorial(n)))