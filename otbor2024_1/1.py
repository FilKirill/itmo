num = 0
sp = []
while len(sp) <= 10 ** 8:
    if len(str(num)) * 3 == len(str(bin(num)[2:])):
        sp.append(num)
    num += 1
print(sp[10 ** 8 - 2])
"""
1057806682
"""