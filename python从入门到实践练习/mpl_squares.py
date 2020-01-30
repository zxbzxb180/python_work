#coding=gbk
import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap = plt.cm.Blues,edgecolor='none',s=40)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,5100,0,25000000])

#plt.savefig('square_plot.png',bbox_inches='tight')
plt.show()

