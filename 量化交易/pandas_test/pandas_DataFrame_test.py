#-*-encoding:utf-8 -*-
import pandas as pd
import numpy as np

#字典创建
df = pd.DataFrame({'one': [1., 2., 3., 5], 'two': [1., 2., 3., 4.]})
print(df)

#二维ndarray创建
data = np.zeros((3,)).astype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 1., 'hello'), (2, 2., 'world'), (3, 3., '!')]
df2 = pd.DataFrame(data, index=['first', 'second', 'third'], columns=['C', 'A', 'B'])
print(df2)

#series组成的字典形式的创建
data2 = {
    'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two': pd.Series([1., 2., 3., 4], index=['a', 'b', 'c', 'd']),
}
df3 = pd.DataFrame(data2, index=['d', 'b', 'a'], columns=['two', 'three'])
print(df3)

#字典的列表形式创建
data3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df4 = pd.DataFrame(data3, index=['first', 'second'], columns=['a', 'c', 'b', 'd'])
print(df4)

#字典的字典创建
df5 = pd.DataFrame()