def fun(num, end):
    if num > end:
        return 0
    if num == end:
        return 1
    dp = [0] * (end + 1)
    dp[num] = 1
    for i in range(num, end +1):
        if i + 1 <= end:
            dp[i+1] += dp[i]
        if ((i * 3) // 2 ) <= end:
            dp[(i * 3) // 2] += dp[i]
        if i * 2 <= end:
            dp[i * 2] += dp[i]
    return dp[end]


print(fun(10, 19) * fun(19, 33) * fun(33, 51) * fun(51, 5094))
print(fun(10, 18) * fun(18, 35) * fun(35, 51) * fun(51, 5094))
print(fun(10, 17) * fun(17, 31) * fun(31, 51) * fun(51, 5094))
print('answer', 312)