for _ in range(int(input())):
    n = int(input())
    coor = [list(map(int, input().split())) for i in range(n)]
    tangens = []
    for i in range(1, n):
        x, y = coor[i]
        tangens.append([(y - coor[0][1]) / (x - coor[0][0]), i + 1])
    dp = [1] * len(tangens)
    put = [-1] * len(tangens)
    for i in range(len(tangens)):
        for j in range(i):
            if tangens[j][0] < tangens[i][0]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    put[i] = j
    res = []
    curr = dp.index(max(dp))
    while curr != -1:
        res.append(tangens[curr][1])
        curr = put[curr]
    res.reverse()
    print(max(dp))
    print(*res)