print('a', 'b', 'c', 'd', 'e', sep=' ')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    t1 = not ((a * b) <= (not (b) * c))
                    t2 = not (((not (b)) * c) <= ((not (c)) * d))
                    t3 = not (((not (b)) * c) <= ((not (c)) * d))
                    t4 = not (((not (c)) * d) <= ((not (d)) * e))
                    if (not ((not (t1 <= t2)) <= (not (t2 <= t3)))) == 1:
                        print(a, b, c, d, e)
