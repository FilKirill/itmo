a = 50890368413
b = 93601980590
c = 172160883161

d = c - b - a
while d > 0:
    print(d)
    c = b
    b = a
    a = d
    d = c - b - a
