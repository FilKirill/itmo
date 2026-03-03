for n in range(2, 1000):
    chclitel = 171
    znam = 255 * (4 ** (n - 1))
    disit = []
    ost = chclitel % znam
    for i in range(100):
        ost *= 16
        digit = ost // znam
        disit.append(digit)
        ost = ost % znam
    if sum(disit) == 441:
        print(n)
        break
