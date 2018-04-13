class Kan(object):
    def __init__(self,name):
        self.name = name
    def sun(self):
        print(self.name,'呵呵')
    def wen(self):
        print(self.name,'哈哈')
thor_gun = Kan('我去')
thor_gun.sun()
thor_gun.wen()
thor_gun.color = 'jj'
thor_gun.type = 'hh'
thor_gun.theprince = 888
print('我去的:,颜色%s，价钱%s,类型%d'%(thor_gun.color,thor_gun.type,thor_gun.theprince))
print('*'*25)
