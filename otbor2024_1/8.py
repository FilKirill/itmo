sp = [1]
su = 1
while len(sp) < 10 ** 7 - 100:
    ost = su % 13
    su += ost
    sp.append(ost)
sp = sp[::-1]
print(sp[199], sp[99998])
