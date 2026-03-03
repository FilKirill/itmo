def fib(n):
    cnt = 0
    r = 0
    a = 1
    b = 1
    d = 0
    s = 0
    while n > 0:
        cnt += 1
        if cnt > 10000:
            return
        d = n % 2
        if d == 1:
            r = r + b
        if d + s < 2:
            n = n // 2
            s = d
        t = a
        a = b
        b = t + b
    return r


for n in range(1, 100000):
    if fib(n) == 272:
        print(n)
