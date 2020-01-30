# coding=gbk
while True:
	
	try:
		a = input("请输入两个数字：")
		if a == 'q':
			break
		a = int(a)
		b = input()
		b = int(b)
		c = a+b
	except ValueError:
		print("请按规定输入数字\n")
	else:
		print(str(c)+"\n")


