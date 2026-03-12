for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                if ((((not (B)) <= (not (A))) <= (not (B))) or (((not (A)) <= (not (C))) and (not (C))) or (not (A <= (not (D))))) == 0:
                    print((D <= C) == (A <= B))
# 6 7 8 10