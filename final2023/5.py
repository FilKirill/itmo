for n in range(1, 10**8):
    N = n
    mas = [2, 3, 1]
    cnt = 0
    i = 0
    d = 3
    while sum(mas) != 0:
        if i < 3:
            if mas[i] != 0 and N % d == 0:
                N = N // d
                mas[i] = mas[i] - 1
            else:
                d = d + 2
                i = (i + 1)
        else:
            break
    else:
        if N == 1:
            print(n)
            break