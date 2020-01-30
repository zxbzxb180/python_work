def angular(n):
    x = 1
    a = [1]
    while x <= n:
        yield a
        l1 = [0]+a
        l2 = a+[0]
        a = []
        x += 1
        for i in range(x):
            a.append(l1[i]+l2[i])

for t in angular(10):
    print(t)