import pygame
from gws import *
pygame.mixer.init()
pygame.mixer.music.load('/home/share/MC天佑 - 又.mp3')
pygame.mixer.music.play()
class PlaneGame(object):
    """飞机大战主游戏类"""
    # 初始化方法

    def __init__(self):
        print("游戏初始化")
        """在开始游戏我们做这么几件事
		1 创建游戏窗口
		2 创建游戏时钟
		3 调用创建精灵和精灵组的方法 （私有方法）
		"""
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def start_game(self):
        """在开始游戏这里我们需要做下面几件事"""
        while True:
            # 1 设置帧率
            self.clock.tick(60)
            # 2 事件监听 主要是要监听我们鼠标 键盘的一些事件
            self.__event_handler()
            # 3 碰撞检测 碰撞检测的内容比较  在这里我还没有定义 现在需要补上
            self.__check_collide()
            # 4 更新精灵和精灵组
            self.__update_sprites()
            # 5  更新显示
            pygame.display.update()
            # 在上面  我们调用类方法 并且关于帧率的设置
            # 更新精灵组 碰撞检测 刷新屏幕这些事情 是要实时检测的
            # 所以我写在游戏循环里面
            # 没1/60秒 就会调用一次

    # 创建精灵和精灵组
    def __create_sprites(self):
        bg1 = Background()
        # True 就表示是第二张图片
        bg2 = Background(True)
        # 首先你要知道 你需要先 创建背景精灵 需要把精灵的修改一下
        # bg1 = Background('images/background.png')
        # bg2 = Background('images/background.png')
        # # 我们发现 两张图片的位置我们需要设置一下
        # bg2.rect.y = -bg2.rect.height
        # 我们已经创建了背景精灵  我们接下来可以创建一个背景精灵组
        # 背景组 把我们的背景扔进 背景精灵组
        #------------------------------------------
        # 英雄
        self.hero = Hero(0)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄组
        self.hero_group = pygame.sprite.Group(self.hero)

    # 事件监听
    def __event_handler(self):

        # 在这里我先写 事件监听  为啥呢？在调试过程中我好关闭窗口呀
        for event in pygame.event.get():
            # 另外一个方案 返回按键元组  这个我们观察一下就知道了
            # 如果 某个按键按下 对应的值应该会是
            key_pressed = pygame.key.get_pressed()
            key_pressed1 = pygame.key.get_pressed()
            if key_pressed[pygame.K_KP1]:
            	self.hero.fire()
            if key_pressed[pygame.K_RIGHT]:
                print("向右边移动")
                # 给英雄一个移动速度
                self.hero.speed = 8
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -8
                print("向左边移动")

            elif key_pressed[pygame.K_UP]:
                print("向上边移动")
                self.hero.speed1 = -8

            elif key_pressed[pygame.K_DOWN]:
                print("想下边移动")
                self.hero.speed1 = 8
            else:
                self.hero.speed = 0
                self.hero.speed1 = 0

            # pygame.event.get():这是 获取到我们所有的事件
            if event.type == pygame.QUIT:

                # 哈哈 我调用方法 是不是相当于可以关闭我们的窗口啦！！！
                # 在开发的过程中需要  有这种思想 专门的事情由专门的方法去做
                self.__game_over()
                # event.type 相当于说之前 是通过我们按键盘或者
                # 移动鼠标 产生事件
                # 那么现在呢  是我们自己创造一个事件 每秒执行一次
                #  然后我们去监听我们自己 让 系统去每秒调用的事件
                # 如果调到 那就说明监听成功
                # 那么既然监听监听成功 我需要在监听成功后
                # 去创建敌机  因为我的目的 就是每秒创建一家敌机
            elif event.type == CREATE_ENEMY_EVENT:
                # 因为我的敌机精灵类还没有写
               
                # 我这里就先输出一下
                # 其实这一步  我们完全可以先运行一下
                # 看看有没有出错  看看是不是每秒调用一次
                print("新的敌机产生")
                # 我们添加了敌机  但是但是但是
                # 没有刷新呀！
                self.enemy_group.add(Enemy())
            #elif event.type == HERO_FIRE_EVENT:
                #self.hero.fire()
                #self.hero1.fire()
            '''
            if key_pressed1[pygame.K_SPACE]:
            	self.hero1.fire()
            if key_pressed1[pygame.K_d]:
                print("向右边移动")
                # 给英雄一个移动速度
                self.hero1.speed = 8
            elif key_pressed1[pygame.K_a]:
                self.hero1.speed = -8
                print("向左边移动")

            elif key_pressed1[pygame.K_w]:
                print("向上边移动")
                self.hero1.speed1 = -8

            elif key_pressed1[pygame.K_s]:
                print("想下边移动")
                self.hero1.speed1 = 8
            else:
                self.hero1.speed = 0
                self.hero1.speed1 = 0
            '''
    # 更新精灵和精灵组
    def __update_sprites(self):
        """更新精灵组"""
        # 我们这一步  先更新背景组
        # 刷新位置
        # self.back_group.update()
        # # 绘制到屏幕上   类似blit
        # self.back_group.draw(self.screen)

        # self.enemy_group.update()
        # self.enemy_group.draw(self.screen)

        # self.hero_group.update()
        # self.enemy_group.draw(self.screen)

        #  到这里我们就可以简写代码了 改造 看了比较清爽
        for xxx in [self.back_group, self.enemy_group, self.hero_group, self.hero.bullets, self.hero1.bullets]:
            xxx.update()
            xxx.draw(self.screen)

    def __check_collide(self):
        """接下来我们就需要完成碰撞检测"""
        # 1 子弹摧毁飞机
        # 子弹炸毁敌机 的情况：
        # 地一个参数和第二个参数是要参与碰撞检测的精灵
        # 地三个参数为 Ture的时候 就是当碰撞的时候 被碰撞的精灵从精灵组移出
        pygame.sprite.groupcollide(
            self.enemy_group, self.hero.bullets,True, True)
        # 2 敌机撞毁飞机
        enemies = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, True)
        #pygame.sprite.groupcollide(
            #self.enemy_group#, self.hero1.bullets, True, True)
        #enemies1 = pygame.sprite.spritecollide(
            #self.hero1, self.enemy_group, True)
        # 判断列表时候有内容
        if len(enemies) == 0:
            # 让英雄牺牲
            self.hero.kill()
            self.hero.rect.x = -SCREEN_RECT.width
        '''
        if len(enemies1) == 1:
            
            self.hero1.kill()
            self.hero1.rect.x = -SCREEN_RECT.width
        '''
        if self.hero.rect.x == -SCREEN_RECT.width: # and self.hero1.rect.x == -SCREEN_RECT.width:
            # 结束游戏
            self.__game_over()

    def __game_over(self):
        """游戏结束"""
        print("游戏结束")
        # 这是pygame提供的卸载模块的功能
        pygame.quit()
        # 这是python本身提供的退出脚本的功能
        exit()
        # 总结 ：我们需要先卸载我们的pygame模块  然后退出我们的脚本



# 这个方法就是在我当前方法内生效 在其他模块调不到
if __name__ == "__main__":
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game()