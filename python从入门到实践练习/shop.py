# coding=gbk
class Re():
	def __init__(self,name,type_):
		self.name = name
		self.type_ = type_
		self.number1 = 0
	def set_number(self,number1):
		self.number1 = number1
	def inc_number(self,number1):
		self.number1+=number1
	def describe(self):
		print("�����������ǣ�"+self.name)
		print("�����������ǣ�"+self.type_)
		print("�Ͳ�������"+str(self.number1))
	def open_(self):
		print("����Ӫҵ")
class Ice(Re):
	def __init__(self,name,type_):
		super().__init__(name,type_)
		self.flavors = ['a','b','c']
	def sell(self):
		print(self.flavors)

		
			
