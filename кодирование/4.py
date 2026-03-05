import math

n = 19968

for m in range(1, 10 ** 6):
    if n % m == 0 and m % 16 == 0:
        for k in range(1, 10 ** 5):
            if k * (math.ceil(math.log(m, 2))) + k * 5 == 208 * 8:
                if k * (math.ceil(math.log(m // 16, 2))) + k * 5 == 144 * 8:
                    print(n // m)
