def is_odd(n):
    return n % 2 == 1

a = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

print(list(a))

#用筛选函数对列表进行筛选