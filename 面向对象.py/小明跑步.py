class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return"我叫 %s 体重 %.2f 公斤"%(self.name, self.weight)

    def run(self):
        print("%s 喜欢跑步，跑步锻炼身体"%self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货,吃完这顿就减肥"%self.name)
        self.weight += 1

xiaoming = Person("小明",75)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)
