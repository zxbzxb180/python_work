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
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一个Play按钮
	play_botton = Button(ai_settings,screen,"Play")
	
	#创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	
	#创建一个外星人
	alien = Alien(ai_settings,screen)
	
	#创建一个用于存储子弹的编组
	bullets = Group()
	
	#创建一个存储外星人的编组
	aliens = Group()
	
	game_functions.create_fleet(ai_settings,screen,ship,aliens)
	
	#设置背景颜色
	bg_color = (230,230,230)
	
	#开始游戏主循环
	while True:
		
		#监视键盘和鼠标事件
		game_functions.check_events(ai_settings,screen,stats,play_botton,ship,aliens,bullets)						
		
		if stats.game_active:
			ship.update()				
			game_functions.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)		
			game_functions.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		
		#更新屏幕上的图像，并切换到新屏幕
		game_functions.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_botton)
		
		
run_game()

