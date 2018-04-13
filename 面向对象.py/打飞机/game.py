import pygame
#初始化方法
pygame.init()
#初始化游戏窗口
screen = pygame.display.set_mode((480,700))
#载入图片
bg = pygame.image.load("./images/background.png")
#确定英雄的初始化位置 返回的是一个坐标系(150,500,102,126)
hero_rect = pygame.Rect(200,500,102,126)
#绘制的屏幕上
screen.blit(bg,(0,0))
#载入英雄图片
hero = pygame.image.load("./images/me1.png")
#绘制到屏幕上
screen.blit(hero,hero_rect)
#刷新屏幕
pygame.display.update()
#时钟对象
clock = pygame.time.Clock()
#英雄飞机的y轴的值
hero_rect = pygame.Rect(200,500,102,126)
'''
import random
y = hero_rect.y
height = hero_rect.height
bottom = y + height
y = bottom - height
def __init__(self):
    super().__init__(".images/enemy1.png")
self.spead = random.randint(1,3)
self.rect.bottom = 0
max_x = SCREEN_RECT.width - self.rect.width
self.rect.x = random.randint(0,max_x)
'''
while True:
        # 可以通过hero_rect.y获取到当前飞机的y值
        # hero_rect.x hero_rect.height hero_rect.width
        # top bottom left right
        # 每循环一次  y轴的值 - 500
        hero_rect.y -= 1
        # print(hero_rect.y)
        if hero_rect.y + hero_rect.height <= 0:
            hero_hero.y = 700
        # if hero_rect.y <= 0:
        #       hero_rect.y = 700

        screen.blit(bg,(0,0))
        screen.blit(hero,hero_rect)        
        pygame.display.update()
        clock.tick(60)
        # 监听事件 pygame.event.get()
        # print(type(pygame.event.get()))
        for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN:
                        if event.key == 113:
                                print("我爱你就像老鼠爱大米")

                # if event.type == pygame.KEYNOWN:
                #       if event.key == 113:
                #               pygame.quit()
                #               exit()
                        # pygame.quit()
                        # exit()

                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()



pygame.quit()
