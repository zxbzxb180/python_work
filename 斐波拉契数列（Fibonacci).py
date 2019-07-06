def fib(n):
    L = [1]
    x, a, b = 0, 0, 1
    while x<n:
        yield L
        L.append(a+b)
        a, b = b, a+b
        x += 1

def fib2(n):
    if n==1 or n==2:
        return 1
    return fib2(n-1)+fib2(n-2)





for i in fib(10):
    print(i)

print(fib2(10))