import math

sp = ['A', 'B', 'C']
tri = ['A', 'B']
cnt1 = 0
cnt2 = 0
stroka = ''

for i in range(1, 10 ** 6):
    stroka += sp[cnt1]
    cnt1 = (cnt1 + 1) % 3
    if i % 2 == 0:
        stroka += 'A'
    if i % 3 == 0:
        stroka += tri[cnt2]
        cnt2 = (cnt2 + 1) % 2
    if len(stroka) % 3 == 0:
        petya = len(stroka) * 2
        troiki = set()
        for j in range(0, len(stroka), 3):
            troiki.add(stroka[j:j + 3])
        vasya = (len(stroka) // 3) * math.ceil(math.log2(len(troiki)))
        if petya - vasya == 40:
            print(len(stroka))
            break
