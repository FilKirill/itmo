def fun(t):
    r = t[0]
    i = 1
    while i < 4:
        temp = r
        while r != t[i]:
            if r > 24000:
                break
            r = r + temp
        i = i + 1
    return r


sp = [7]
while sp[-1] <= 23023:
    sp.append(sp[-1] + 7)
for x in range(len(sp)):
    for y in range(len(sp)):
        if fun([7, sp[x], sp[y], 23023]) == 23023:
            print(sp[x], sp[y])

# 77 1001
