#coding=gbk
import unittest
from (11-1) import con
class ConTestCase(unittest.TestCase):
	"""����11-1.py"""
	def test_con(self):
		address = con('����','�й�')
		self.assertEqual(address,'����,�й�')
	def test_con2(self):
		address = con('����','�й�','50000')
		self.assertEqual(address,'����,�й�-�˿�:50000')
unittest.main()
