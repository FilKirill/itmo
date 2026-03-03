stroka = list('AA')
bukvi = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
"""for b in bukvi[:5]:
    new = []
    for i in stroka:
        new.append(b)
        new.append(b)
        new.append(i)
    new.append(b)
    new.append(b)
    stroka = new
    print(stroka)"""
a = 961376769
while a > 0:
    print(a % 3)
    a //= 3
print(bukvi[-16])
print(bukvi[-24])