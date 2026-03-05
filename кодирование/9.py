import math

for z in range(10 ** 6, 0, -1):
    petya = 256 * math.ceil(math.log(z, 2))
    vasya_162 = 162 * (8 + math.ceil(math.log(z, 2)))
    vasya_163 = 163 * (8 + math.ceil(math.log(z, 2)))
    if vasya_162 < petya and vasya_163 > petya:
        print(z)
        break
