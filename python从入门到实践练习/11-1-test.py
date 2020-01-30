#coding=gbk
import unittest
from (11-1) import con
class ConTestCase(unittest.TestCase):
	"""测试11-1.py"""
	def test_con(self):
		address = con('株洲','中国')
		self.assertEqual(address,'株洲,中国')
	def test_con2(self):
		address = con('株洲','中国','50000')
		self.assertEqual(address,'株洲,中国-人口:50000')
unittest.main()
