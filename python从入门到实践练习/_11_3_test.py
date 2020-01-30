#coding=gbk
import unittest
from _11_3 import Employee
class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.employee = Employee('x','c',5000)
		
	def test_default_raise(self):
		money = self.employee.money
		self.employee.give_raise()
		self.assertEqual(self.employee.money,money+5000)
	def test_custom_raise(self):
		money = self.employee.money
		self.employee.give_raise(10000)
		self.assertEqual(self.employee.money,money+10000)
unittest.main()
