import math

a = math.ceil(math.log(math.comb(16, 8), 2))
for n in range(1, 1000):
    if n ** 2 - (n / 4) ** 2 * 14 == 81 * 8:
        print(n)
        break
