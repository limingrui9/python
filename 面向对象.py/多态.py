class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 蹦蹦跳跳玩耍..."% self.name)
class XiaoTianDog(Dog):
    def game(self):
        print("%s 可以飞天玩耍..."% self.name)
class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s和%s快乐的玩耍..."%(self.name, dog.name))
        dog.game()
#1.创建一个狗对象
#wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
wangcai.game()
#2.创建一个小明对象
xiaoming = Person("小明")
#3.让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
