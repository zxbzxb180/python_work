#斐波拉契数列的生成器
def fib(n):
    L = [1]
    x, a, b = 0, 0, 1
    while x<n:
        yield L
        L.append(a+b)
        a, b = b, a+b
        x += 1

#求斐波拉契数列第n项
def fib2(n):
    if n in [1, 2]:
        return 1
    return fib2(n-1)+fib2(n-2)

#循环生成器打印
for i in fib(10):
    print(i)

#打印斐波拉契数列第n项
#print(fib2(10))

def fib3(n):
    x, a, b = 0, 0, 1
    while x < n:
        print(b, end=' ')
        x+=1
        a, b = b, a+b

fib3(10)

import copy
copy.deepcopy()
