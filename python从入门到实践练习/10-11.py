#coding=gbk
import json
number = input("请输入您喜欢的数字：")
with open('number.json','w') as n_obj:
	json.dump(number,n_obj)

