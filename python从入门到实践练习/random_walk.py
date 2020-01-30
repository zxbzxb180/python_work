#coding=gbk
from random import choice

class RandomWalk():
	"""һ����������������ݵ���"""
	def __init__(self,num_points = 5000):
		"""��ʼ���������������"""
		self.num_points = num_points
		
		#�������������ʼ�ڣ�0,0��
		self.x_values = [0]
		self.y_values = [0]
		
	def fill_walk(self):
		"""����������������ĵ�"""
		
		#����������ֱ���б�ﵽָ������
		while len(self.x_values) < self.num_points:
			#����ǰ�������Լ����������ǰ���ľ���			
			x_step = self.get_step()			
			y_step = self.get_step()
			
			#�ܾ�ԭ��̤��
			if x_step ==0 and y_step ==0:
				continue
				
			#������һ�����x,y
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
	def get_step(self):
		"""����ÿ�������ľ���ͷ���"""
		return choice([1,-1])*choice([0,1,2,3,4])
