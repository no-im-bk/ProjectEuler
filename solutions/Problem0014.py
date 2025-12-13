# use top down dynamic programming to cache the results (for values under 1 mil) as we work up from the bottom
table = [-1 for _ in range(1000000)]
table[1] = 1

def step(x):
    if x < 1000000 and table[x] > 0:
        return table[x]
    if x % 2 == 0:
        ans = 1 + step(x//2)
    else:
        ans = 1 + step(3*x + 1)
    if x < 1000000:
        table[x] = ans
    return ans

ans = (1, 1)
for x in range(1, 1000000):
    s = step(x)
    if s > ans[0]:
        ans = (s, x)

print(ans)