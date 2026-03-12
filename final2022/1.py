from fractions import Fraction

znam = 3
su = Fraction(1, 3)
for i in range(2, 31):
    znam *= 2
    su += Fraction(1, znam)

res = []
while su.numerator != 0:
    su *= 16
    res.append(int(su.numerator / su.denominator))
    su = Fraction(su.numerator % su.denominator, su.denominator)
print(sum(res))
# 78
"""print(drob)
res = []
while drob != 0:
    drob *= 16
    res.append(int(drob))
    if res[-1] == 0:
        break
    drob = float(f'0.{str(drob).split(".")[1]}')
print(sum(res))"""
