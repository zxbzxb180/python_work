# coding=gbk
name = input("请输入您的姓名：")

with open('pi.txt','a') as file_object:
	file_object.write(name)
	

	
