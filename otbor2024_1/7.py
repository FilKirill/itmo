for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                s1 = x1 ^ (not (x2))
                c1 = x1 and (not (x2))
                s2 = x2 ^ (not (x3))
                c2 = x2 and (not (x3))
                s3 = x3 ^ (not (x4))
                c3 = x3 and (not (x4))
                s4 = x4 ^ (not (x1))
                c4 = x4 and (not (x1))

                r1 = s1 or c2
                r2 = s2 and c3
                r3 = s3 or c4
                r4 = s4 and c1
                if (r1 or r2 or r3 or r4) == 0:
                    print(x1, x2, x3, x4)
