for _ in range(int(input())):
    a, e, n = map(int, input().split())
    fabric = [list(map(int, input().split())) for i in range(n)]
    m = int(input())
    artefacts = [list(map(int, input().split())) for i in range(m)]
    q = int(input())
    resurs = [0] * n
    rabotaet = [True] * n
    deist = {}
    for i in range(q):
        zap = input().split()
        if int(zap[0]) not in deist:
            deist[int(zap[0])] = []
        deist[int(zap[0])].append(zap[1:])
    for i in range(1, max(deist.keys()) + 1):
        a += e
        if i in deist:
            for j in deist[i]:
                if j[0] == 'OFF':
                    rabotaet[int(j[1]) - 1] = False
                elif j[0] == 'ON':
                    rabotaet[int(j[1]) - 1] = True
        for j in range(n):
            if rabotaet[j]:
                racx, proizod = fabric[j]
                if a >= racx:
                    a -= racx
                    resurs[j] += proizod
        if i in deist:
            for d in deist[i]:
                if d[0] == 'CREATE':
                    recept = artefacts[int(d[1]) - 1]
                    res = []
                    for j in range(n):
                        if resurs[j] < recept[j]:
                            res.append(j + 1)
                    if not res:
                        for j in range(n):
                            resurs[j] -= recept[j]
                        print("OK")
                    else:
                        print(f"FAIL: missing {min(res)}")
