import math

# an ugly oneliner that searches for the answer
print([(int(math.sqrt(c**2 - b**2)) * b * c,int(math.sqrt(c**2 - b**2)), b ,c ) for c in range(1001) for b in range(min(c,1001 - c)) if int(math.sqrt(c**2 - b**2)) ** 2 == c**2 - b**2 and int(math.sqrt(c**2 - b**2)) + b + c == 1000])