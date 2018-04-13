"""
这是我们刚刚说的  另外一个需要设计的模块
在这个模块  放一些常用工具和 基础类  和精灵类
在其他模块调用
"""
import pygame
import random
# 设置游戏屏幕小大 这是一个常量
# 常量见名知意 就是不需要猜测的数字的含义 就是一个固定的数值
# 通过一处修改 其他地方也能生效 统一控制
SCREEN_RECT = pygame.Rect(0, 0, 480,700)

# 我们的父类需要考虑这几个问题
# 1 通用性 2 属性有哪些  方法有哪些   将来谁要用
# 我们自己去定制的精灵类  需要继承 pygame提供的精灵类
"""
我们需要定义的属性有：
image-->图片
rect--->坐标
speed -->速度
"""

# 接下来我们就开始写我们敌机方面的内容 （产生敌机）
# 我先定义一个事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 我们还可以定义一个事件常量 （发射子弹）
HERO_FIRE_EVENT = pygame.USEREVENT + 1



class GameSprite(pygame.sprite.Sprite):
	"""游戏精灵的基础类"""
	# 我们其实可以给我们的基础类的速度 设置一个默认值
	def __init__(self,new_image,new_speed=1):
		super().__init__()
		# 我们需要以下3个属性
		# 考虑到通用性  我们需要改造一下代码
		# pygame.image.load pygame提供的方法 主要是加载图片
		self.image = pygame.image.load(new_image)
		# self.image.get_rect() 获取图片的宽高 get_rect() 是pygame提供
		self.rect = self.image.get_rect()
		# 这是将来精灵的移动速度 精灵有：英雄精灵 背景精灵 敌机精灵 子弹精灵
		self.speed = new_speed

	def update(self):
		# 默认垂直方向移动 （这个时候我就要有一个概念 坐标系的y轴控制垂直
		self.rect.y += self.speed


# 那么以上就是我们游戏的基础类 接下来我们需要设置我们的 背景类
# 首先我们需要先明确我们的背景类  继承自我们的游戏精灵类
class Background(GameSprite):
	"""背景精灵类"""
	def __init__(self,is_alt=False):
		"""is_alt 判断是否为另外一张图像
		False表示第一张图像 
		True表示另外一张图像     我们最开始说了  我们是2张图像交替
		在这里我先设置一下 vim快捷键
		"""
		# 因为背景图片是固定的  所以我们可以在背景精灵类直接传图片
		super().__init__('./images/background.png')
		if is_alt:
			# 如果是地二张图片 我们让他的初始位置为 -self.rect.height
			self.rect.y = -self.rect.height

	def update(self):
		# 1 调用父类的方法实现 这是实现父类方法
		super().update()
		# 2 判断是否移除屏幕 如果移出屏幕 我们就要将图像设置到屏幕到上方
		# SCREEN_RECT.height 这是我们自己设置的常量  我们可以往上看
		# 其实到这一步 我们就已经把我们的背景类设计完了 接下来我们就去我们的主程序模块调用就行了
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height

# 接下来我们就要设置我们的敌机类
# 我们的敌机类 同样也是继承自我们的精灵基类
class Enemy(GameSprite):
	"""敌机精灵类"""
	def __init__(self):
		# 1 调用父类方法 创建敌机精灵类 并且指定敌机图像
		super().__init__('./images/enemy1.png')
		# 2 设置敌机初始速度 稍后设置 （随机数）
		# 我的sublime 没有花事件去调  老是跟我发脾气
		self.speed = random.randint(1, 3)
		# 3 设置敌机的随机初始位置 稍后设置
		# self.rect.y  = self.rect.bottom - self.rect.height
		self.rect.bottom = 0
		# 敌机x轴最大值 需要用屏幕的宽度-敌机自身的宽度
		max_x = SCREEN_RECT.width - self.rect.width
		# 随机一个位置
		self.rect.x = random.randint(0, max_x)


		# 我们发现。。。。。敌机出来的位置在 一条线上
		# 说明  x轴的位置一直没有变 

		def update(self):
			# 1 调用父类方法
			super().update()

			# 2 判断是否飞出屏幕 如果是 需要敌机从精灵组删除
			if self.rect.y >= SCREEN_RECT.height:
				print("敌机飞出屏幕")
				# 移出屏幕  就销毁
				self.kill()
# 接下来我们就设计英雄类和子弹类

# 英雄精灵类
class Hero(GameSprite):
	"""英雄精灵类"""
	def __init__(self,a):
		# 英雄的初始速度我设置为0
		super().__init__('./images/me1.png',0)

		# 设置初始位置 这是是让我英雄X轴的中心点等于屏幕X轴中心点
		self.rect.centerx = SCREEN_RECT.centerx + a
		# 这里是设置我飞机的y轴
		self.rect.bottom = SCREEN_RECT.bottom 

		# 子弹组
		self.bullets = pygame.sprite.Group()
		# 这样 我们的子弹精灵组 就创建完毕了 我们就要去fire里面修改我们的
		# 方法
		self.speed1 = 0

	def update(self):
		# 飞机水平移动
		self.rect.x += self.speed
		self.rect.y += self.speed1
		# 控制英雄边界 屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right >SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
		if self.rect.top < 0:
			self.rect.top = 0
	def fire(self):
		# 英雄的方法。。。发射子弹  是一个动作  是一个行为 。。。
		print("发射子弹....")

		for i in (1,2,3):
			# 子弹精灵 我们在 英雄的这个fire（）方法里面去创建
			#1 创建 子弹精灵
			bullet = Bullet()
			gws = Bullet()
			sst = Bullet()
			#2 设置精灵位置
			bullet.rect.bottom = self.rect.y -20
			bullet.rect.centerx = self.rect.centerx
			gws.rect.bottom = self.rect.y -20
			gws.rect.centerx = self.rect.centerx +15
			sst.rect.bottom = self.rect.y -20
			sst.rect.centerx = self.rect.centerx -15
			#3 将精灵添加到精灵组
			
			self.bullets.add(bullet,gws,sst)


class Bullet(GameSprite):
	"""子弹精灵"""
	def __init__(self):
		super().__init__('./images/bullet1.png',-10)
	def update(self):
		super().update()
		# 判断是否超出屏幕
		if self.rect.bottom < 0:
			self.kill()
