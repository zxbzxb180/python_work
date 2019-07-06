a = sorted([36, 5, -12, 9, -21], key=abs, reverse=True) #abs是取绝对值函数, reverse表示倒序
print(a)


#sorted是临时排序函数，不会改变原列表顺序
#sort是永久排序函数，会改变原列表顺序