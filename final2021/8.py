n = int(input())
for t in range(n):
    test = set()
    for i in range(10):
        test.add(input())
    if t != n:
        _ = input()
    if len(test) != 1:
        print("Incorrect")
    else:
        cnt = 0
        for i in test.pop().split('.'):
            if '#' in i:
                cnt += 1
        if cnt == 1:
            print('Negative')
        elif cnt == 3:
            print('Positive')
        else:
            print("Incorrect")
