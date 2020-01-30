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
		print("餐厅的名字是："+self.name)
		print("餐厅的类型是："+self.type_)
		print("就餐人数："+str(self.number1))
	def open_(self):
		print("正在营业")
class Ice(Re):
	def __init__(self,name,type_):
		super().__init__(name,type_)
		self.flavors = ['a','b','c']
	def sell(self):
		print(self.flavors)

		
			
