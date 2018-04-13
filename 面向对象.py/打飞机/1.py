import pygame

#需要把我们的游戏逻辑写在初始化方法和结束方法之间
pygame.init()
#初始化游戏窗口
screen = pygame.display.set_mode((480,700))
#加载图片
bg = pygame.image.load("./images/background.png")


#确定英雄初始化位置，返回一个坐标系(150,500,102,126)
hero_rect = pygame.Rect(200,500,102,126)

#绘制到屏幕上
screen.blit(bg,(0,0))
#载入英雄图片
hero = pygame.image.load("./images/me1.png")
#绘制到屏幕上
screen.blit(hero,hero_rect)
#刷新屏幕
pygame.display.update()


#时钟对象
clock = pygame.time.Clock()




y= 500
while True:
    y-=1
    hero_rect = pygame.Rect(200,y,102,126)
    screen.blit(hero,hero_rect)
    pygame.display.update()
    clock.tick(60)





pygame.quit()
