#coding=gbk
class Employee:
	def __init__(self,lastname,firstname,money):
		self.lastname = lastname
		self.firstname = firstname
		self.money = money		
	def give_raise(self,add=5000):
		self.money +=add

