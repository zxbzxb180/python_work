# coding=gbk
while True:
	
	try:
		a = input("�������������֣�")
		if a == 'q':
			break
		a = int(a)
		b = input()
		b = int(b)
		c = a+b
	except ValueError:
		print("�밴�涨��������\n")
	else:
		print(str(c)+"\n")


