import math

for t in range(1, 10000):
    petya = 2 * 88200 * math.ceil(math.log(65536, 2)) * t
    vasya = 44100 * (math.ceil(math.log(65536, 2)) + math.ceil(math.log(256, 2))) * t
    if petya - vasya >= 20 * 8 * 1024 * 1024:
        print(t)
        break