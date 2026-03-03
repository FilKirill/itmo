import math

a = math.log(65536, 2)
petya = 16 * 88200 * 2
vas = (16 * 44100) + (44100 * 8)
ans = ((20 * 1024 * 1024 * 8) / (petya - vas))
print(math.ceil(ans))