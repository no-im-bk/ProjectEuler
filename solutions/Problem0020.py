# Easy one liner. Do the math, convert to string, and add the digits
import math
print(sum(int(x) for x in str(math.factorial(100))))