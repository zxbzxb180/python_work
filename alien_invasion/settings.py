#coding=gbk
class Settings():
	"""���桶���������֡����������õ���"""
	def __init__(self):
		"""��ʼ����Ϸ�ľ�̬����"""
		#��Ļ����
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)
		
		#�ɴ�������
		self.ship_speed_factor = 1.5
		self.ship_limit = 2
		
		#�ӵ�������
		self.bullet_speed_factor = 3
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 10

		#����������
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_directionΪ1��ʾ�����ƶ���-1��ʾ�����ƶ�
		self.fleet_direction = 1
		
		#��ʲô�����ٶȼӿ���Ϸ����
		self.speedup_scale = 1.5
		
		self.initialize_dynamic_setting()
		
	def initialize_dynamic_setting(self):
		"""��ʼ������Ϸ���ж��仯������"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		#�Ƿ�
		self.alien_points = 1
		
		#fleet_directionΪ1��ʾ�����ƶ���-1��ʾ�����ƶ�
		self.fleet_direction = 1

	def increase_speed(self):
		"""����ٶ�����"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
