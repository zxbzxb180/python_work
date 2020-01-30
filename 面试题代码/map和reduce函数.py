from functools import reduce

def add(x, y):
    return x*10+y

def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]


r = reduce(add, map(char2num, '13579'))
print(r)


def abc(x):
    return x+1
s = map(abc, [1,2])
print(list(s))


#对某个列表用函数进行操作