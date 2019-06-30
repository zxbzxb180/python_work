#coding=gbk
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#����һ��Play��ť
	play_botton = Button(ai_settings,screen,"Play")
	
	#����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��,�������Ƿ���
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#����һ�ҷɴ�
	ship = Ship(ai_settings,screen)
	
	#����һ��������
	alien = Alien(ai_settings,screen)
	
	#����һ�����ڴ洢�ӵ��ı���
	bullets = Group()
	
	#����һ���洢�����˵ı���
	aliens = Group()
	
	game_functions.create_fleet(ai_settings,screen,ship,aliens)
	
	#���ñ�����ɫ
	bg_color = (230,230,230)
	
	#��ʼ��Ϸ��ѭ��
	while True:
		
		#���Ӽ��̺�����¼�
		game_functions.check_events(ai_settings,screen,stats,play_botton,ship,aliens,bullets)						
		
		if stats.game_active:
			ship.update()				
			game_functions.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)		
			game_functions.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		
		#������Ļ�ϵ�ͼ�񣬲��л�������Ļ
		game_functions.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_botton)
		
		
run_game()

