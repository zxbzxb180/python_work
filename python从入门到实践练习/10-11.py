#coding=gbk
import json
number = input("��������ϲ�������֣�")
with open('number.json','w') as n_obj:
	json.dump(number,n_obj)

