# coding=gbk
def animal(name):
	try:
		with open(name) as n_obj:
			name1 = n_obj.read()
	except FileNotFoundError:
		print("文件不存在!")
	else:
		print(name1)
animal('cat.txt')
print("\n")		
animal('dog.txt')		
print("\n")
animal('fish.txt')
