import math

for n in range(1, 10 ** 4):
    for m in range(1, 10 ** 4):
        if 4488 % n == 0 and 4488 % m == 0:
            petya = (4488 // n) * math.ceil(math.log(151 ** n, 2))
            vasya = (4488 // m) * math.ceil(math.log(151 ** m, 2))
            if petya - vasya == 232:
                print(n, m)
                exit()
