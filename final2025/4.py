n = '123456'
res = [1] * 1000
for d in n[1:]:
    new = []
    for j in res:
        new.append(j)
        new.append(d)
        new.append(d)
    res = new

print(res[(209161 % 243) - 1])
print(res[(242758 % 243) - 1])
print(res[(189890 % 243) - 1])
print(399791)