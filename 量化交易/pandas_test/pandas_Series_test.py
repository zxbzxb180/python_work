import pandas as pd
import numpy as np

a = pd.Series([-1.55667182, -1.55777182, -1.454667182, -1.56588667182, -1.67767182], index=['a', 'b', 'c', 'd', 'e']).astype('int8')

#用ndarray数据类型创建Series对象
b = pd.Series(np.random.random(5))

#用字典数据类型创建Series对象
c = pd.Series({'a': 0, 'b': 1, 'c': 2, 'd': 3}, index=['b', 'a', 'd', 'c'])

#以常量数据类型创建Series对象
d = pd.Series(1.)

# print(c.index)
# print(c.values)
# print(c['a'])
# print(c[['a', 'b']])
print(c[:2])