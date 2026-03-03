s = '123456'
n = 6
r = ''
for i in range(n):
    r += s
    s = s[1:] + s[0]
print(r)
print('a', r[(10 ** 8 + 2) % 36 - 1])
print('c', r[(10 ** 8 + 4) % 36 - 1])
print('b', r[(10 ** 8 + 8) % 36 - 1])
print('d', r[(10 ** 8 + 16) % 36 - 1])
print('f', r[(10 ** 8 + 3) % 36 - 1])
print('e', r[(10 ** 8 + 5) % 36 - 1])
print('cedabf')