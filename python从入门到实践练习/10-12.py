#coding=gbk
import json
try:
	with open('number.json') as n_obj:
		number = json.load(n_obj)
except FileNotFoundError:
	number = input("请输入你喜欢的数字：")
	with open('number.json','w') as n_obj:
		json.dump(number,n_obj)
else:	
	print(number)
