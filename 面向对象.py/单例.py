'''
class MusicPlayer(object):
    def __new__(cls,*args,**kwargs):
        #如果不返回任何结果。
        return super().__new__(cls)

    def __init__(self):
        print("初始化音乐播放器")
player = MusicPlayer()
print(player)
'''
'''
class MusicPlayer(object):
    #定义类属性记录单例对象引用
    instance = None
    def __new__(cls,*args,**kwargs):
        #1.判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        #2.返回类属性的单例引用
        return cls.instance
'''

class MusicPlayer(object):
    #记录第一个被创建对象的引用
    instance = None
    #记录是否执行过初始化动作
    init_flag = False
    def __new__(cls, *args, **kwargs):
        #1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        #3.返回类属性保存的对象引用
        return cls.instance
    def __init__(self):
        if not MusicPlayer.init_flag:
            print("初始化音乐播放器")
            MusicPlayer.init_flag = True

#创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)







