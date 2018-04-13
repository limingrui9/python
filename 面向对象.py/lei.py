class Animal(object):
    #这是初始化方法
    def __init__(self):
        self.pin_zhong = "动物"


    def print_name(self):
        print("绿叶给了我初恋般的感觉")



class Dog(Animal):
    def pao(self):
        print("狗在跑")
#重写父类的方法
    def print_name(self):
        #super().print_name()
        print("红花")



#这里是继承   狗类具有动物类的方法
'''        
wanwan = Dog()
wanwan.pin_zhong = "狗"
wanwan.print_name()
wanwan.pao()
'''
class Cat(Animal):
    def miao(self):
        print("猫在喵")
    def cay(self):
        print("猫在哭")
#继承的顺序决定继承的内容
class ZaJiao(Dog,Cat):
    pass
#实例化一个对相
d = Dog()
d.print_name()


'''
a = Animal()
a.pin_zhong = "哈巴狗"
a.print_name()
'''

