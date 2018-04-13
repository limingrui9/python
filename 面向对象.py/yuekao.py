# 第一题
L = []
for i in range(100,901):
    mark = 0
    for j in range(2,i):
        if i%j == 0:
            mark = 1
            break
    if mark == 0:
        L.append(i)
print(L)


print("*"*100)

# 第二题
'''
Menu = ["苹果汁"，"蓝莓汁"，"香蕉汁","黄瓜汁","番茄汁"]
For I in menu:
    Menu[0] = "苹果汁"
    Menu[1] = "番茄汁"
    B = {'番茄汁' : 6}...
'''

# 第三题

class Kao_di_gua:
    def __init__(self):
        self.sheng_shu = 0
        self.sheng_shu_str = "生的鸡"
        self.add_tiao_liaos = 0

    def Kao(self,times):
        self.sheng_shu += times
        if self.sheng_shu > 8:
            self.sheng_shu_str = "烤糊了"

        elif self.sheng_shu > 5:
            self.sheng_shu_str = '烤熟了'
            self.add_tiao_liao.append('苹果蘸酱')
        elif self.sheng_shu > 3:
            self.sheng_shu_str = '半生不熟'

        else:
            self.add_tiao_liaos.append('橄榄油')
            self.sheng_shu_str = '生鸡'

kdg = Kao_di_gua()
kdg.Kao(3)
print(kdg.sheng_shu_str)
kdg.Kao(3)
print(kdg.sheng_shu_str)
print(kdg.add_tiao_liaos)
