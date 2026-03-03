print('x     y     z    d    f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            a = x * y <= (not (y)) * z
            b = y * z <= (not (z)) * x
            c = (not (z)) * y <= (not (y)) * x
            d = (not (z)) * x <= (not (x)) * y
            f = y <= x * z
            print(a, b, c, d, f)
print(2 ** 10)