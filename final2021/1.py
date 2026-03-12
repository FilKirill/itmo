from fractions import Fraction

for x in range(5, 36):
    for y in range(5, 36):
        num1 = Fraction(int('34', x), x ** 2 - 1)
        num2 = Fraction(int('13', y), y ** 2 - 1)
        if num1 + num2 == 1:
            if 2 * (int('101', x)) - (int('102', y)) == 1:
                print(x, y)

# answer 5 7
