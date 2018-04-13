class plants:
    def fyg(self):
        print("放阳光")
    def shooting(self):
        print("放炮")
    def stop(self):
        print("阻挡")
    def go(self):
        print("走")
    def run(self):
        print("跑")
    def shakeyourhead():
        print("摇头")
    def jump(self):
        print("跳")
    def cat(self):
        print("吃")
    def die(self):
        print("死")

ruiflowers_plants = plants()
ruiflowers_plants.name = "向日葵"
ruiflowers_plants.color = "绿色"
ruiflowers_plants.money = 50
print("%s的属性有:\n颜色:%s\n价格%d"%(ruiflowers_plants.name, ruiflowers_plants.color, ruiflowers_plants.money))
print("%s的行为有:"%ruiflowers_plants.name)
ruiflowers_plants.fyg()
ruiflowers_plants1 = "向日葵"
print("内存地址1:",id(ruiflowers_plants),ruiflowers_plants1)
print("*"*50)

peashooter_plants = plants()
peashooter_plants.name = "豌豆射手"
peashooter_plants.color = "绿色"
peashooter_plants.money = 150
peashooter_plants.hp = 300
peashooter_plants.attack = 150
print("%s的属性有:,颜色:%s,价格:%d,血量:%d,攻击%d"%(peashooter_plants.name,peashooter_plants.color,peashooter_plants.money,peashooter_plants.hp,peashooter_plants.attack))
print("%s的行为有:"%peashooter_plants.name)
peashooter_plants.shooting()
peashooter_plants1 = "豌豆射手"
print("内存地址2:",id(peashooter_plants),peashooter_plants1)
print("*"*25)

nuts_plants = plants()
nuts_plants.name = "坚果"
nuts_plants.color = "米黄色"
nuts_plants.money = 100




