for x in range(2):
    for y in range(2):
        for z in range(2):
            if x <= y and y != z:
                print((x <= y) == z)
                print(((x * (not (y))) == (y * z)) <= (y == z))
                print((x <= y) <= (y ^ z))
                print((not (z ^ y)) <= (y <= z))
                print(((not (y)) * z) <= (y == (not (x))))
                print(' ')

