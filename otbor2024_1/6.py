print('A', 'B', 'C', 'D', 'E', 'F')
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                for E in range(2):
                    for F in range(2):
                        if not ((((((not (A)) * B) == (not (C))) <= ((((not (B)) * C) == (not (D))) <= D)) <= (
                                (((not (C)) * D) == (not (E))) <= E)) <= ((((not (D)) * E) == (not (F))) <= F)):
                            print(A, B, C, D, E, F)

