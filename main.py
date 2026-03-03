print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                if a <= (b <= (c <= (d <= e))):
                                    x = (((not (((d <= (b <= (c <= ((not (e)) <= (not (a)))))) <= (not (f))))) <=
                                          (not ((c <= (d <= (a <= (b <= e)))) <= (not (g))))) <=
                                         (not (((not (e)) <= (b <= (a <= (d <= (not (c)))))) <= (not (h)))))
                                    y = (not (((d <= (b <= (c <= ((not (e)) <= (not (a)))))) <= (not (f))))) <= (
                                            (not ((c <= (d <= (a <= (b <= e)))) <= (not (g)))) <= (
                                        (not (((not (e)) <= (b <= (a <= (d <= (not (c)))))) <= (not (h))))))
                                    if ((not x) <= y) == 0:
                                        print(a, b, c, d, e, f, g, h, (not x) <= y)
