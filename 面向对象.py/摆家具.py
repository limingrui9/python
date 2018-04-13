class HousItem:
    def __init__(self,name,area):
        '''
        :param name: 家具名称
        :param area: 占地面积
        '''
        self.name = name
        self.area = area
    def __str__(self):
        return"[%s] 占地面积 %.2f" % (self.name,self.area)

#创建家具
bed = HousItem("席梦思", 4)
chest = HousItem("衣柜",2)
table = HousItem("餐桌",1.5)
print(bed)
print(chest)
print(table)

