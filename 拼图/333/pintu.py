#coding=gbk
import random
 
import pygame
 
# ��ʼ��
pygame.init()
# ���ڱ���
pygame.display.set_caption('ƴͼ��Ϸ')
# ���ڴ�С
s = pygame.display.set_mode((1200, 600))
 
#��ͼ��ͼ
imgMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
 
#�ж�ʤ���ĵ�ͼ
winMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
 
#��Ϸ�ĵ����¼�
def click(x, y, map):
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]
 
#���ҵ�ͼ
def randMap(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        click(x, y, map)
 
# ����ͼƬ
img = pygame.image.load('./tutu.jpg')
#�����ͼ
randMap(imgMap)
#��Ϸ��ѭ��
while True:
    #��ʱ32����,�൱��FPS=30
    pygame.time.delay(32)
    for event in pygame.event.get():
        # ���ڵĹر��¼�
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:      #��굥���¼�
            if pygame.mouse.get_pressed() == (1, 0, 0):     #����������
                mx, my = pygame.mouse.get_pos()     #��õ�ǰ�������
                if mx<498 and my <498:      #�ж�����Ƿ��ڲ�����Χ��
                    x=int(mx/166)       #�������㵽���ĸ�ͼ��
                    y=int(my/166)
                    click(x,y,imgMap)   #���õ����¼�
                    if imgMap==winMap:  #�����ǰ��ͼ�����ʤ�������ͬ,��printʤ��
                        print("ʤ���ˣ�")
    #����ɫ���ɰ�ɫ
    s.fill((255,255,255))
    #��ͼ
    for y in range(3):
        for x in range(3):
            i = imgMap[y][x]
            if i == 8:      #8��ͼ�鲻�û���
                continue
            dx = (i % 3) * 166      #�����ͼƫ����
            dy = (int(i / 3)) * 166
            s.blit(img, (x * 166, y * 166), (dx, dy, 166, 166))
    # ���ο�ͼƬ
    s.blit(img, (600, 0))
    # ˢ�½���
    pygame.display.flip()

