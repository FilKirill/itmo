zap = [1, 1, 2, 1, 1, 2, 1, 1, 2]
t = 0
ddos_cnt = 0
ddos_time = 0
server_time = 0
queue = []
server = []
users = 0
att_cnt = 0
while users < 9:
    queue.append('atck')
    if t % 15 == 0 and len(zap) > 0:
        queue.append(zap[0])
        del zap[0]
    if queue and ddos_time <= t:
        last = queue.pop(0)
        ddos_cnt += 1
        if ddos_cnt <= 30:
            ddos_time = t + 2
        else:
            ddos_time = t + 1
        att_cnt += 1
        if ddos_cnt <= 30 or last in [1, 2] or (last == 'atck' and (att_cnt) % 50 == 0):
            server.append([last, ddos_time])
    if server and server_time <= t and server[0][1] <= t:
        last, arr = server.pop(0)
        if last == 1:
            server_time = t + 10
        elif last == 2:
            server_time = t + 15
        else:
            server_time = t + 3
        if last in [1, 2]:
            users += 1
    t += 1
print(server_time)