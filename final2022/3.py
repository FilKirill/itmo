cnt = 0
print('x0', 'x1', 'x2', 'x3', 'f')
for num in range(18364758544493064720, 18364758544493064720 + 1):
    N = hex(num)
    dvoi = bin(int(N, 16))[2:].zfill(16 * 4)
    sp = []
    for i in range(0, len(dvoi), 4):
        sp.append(list(map(int, list(dvoi[i:i + 4]))))
    sp.reverse()
    res = []
    for x0, x1, x2, x3 in sp:
        print(x0, x1, x2, x3, str((x0 or (x1 and x2)) and (x1 or (x2 and x3)) and (x2 or (x3 and x0))))
"""for num in range(1, 2**64 + 1):
    N = hex(num)
    dvoi = bin(int(N, 16))[2:].zfill(16 * 4)
    sp = []
    for i in range(0, len(dvoi), 4):
        sp.append(list(map(int, list(dvoi[i:i + 4]))))
    sp.reverse()
    res = []
    for x0, x1, x2, x3 in sp:
        res.append(str((x0 or (x1 and x2)) and (x1 or (x2 and x3)) and (x2 or (x3 and x0))))
    if len(res) == 16:
        if '0000001100010111' == ''.join(res):
            cnt += 1
            print(cnt)
print(cnt)
"""
