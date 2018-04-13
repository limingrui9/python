'''
distance = float(input("请输入距离"))
money = 0
sum = 0
for i in range(0,60):
    if distance<=6:
        money = 3
    elif 6<distance and distance <= 12:
        money = 4
    elif 12<distance and distance <= 22:
        money = 5
    elif 22<distance and distance <= 32:
        money = 6
    elif distance>32:
        if (distance-32)%20 == 0:
            money = 6+(distance-32)/20
        else:
            money = 6+int((distance-32)/20)+1

    if sum>=100 and sum<150:
        money = money*0.8
    elif sum>=150 and sum<400:
        money = money*0.5



    sum +=money

    print("一共花了%.2f"%sum)
'''



list=[] #用来记录每个月的地铁费用
allcount = 0    #用来记录一共乘坐多少次地铁
#计算每个月的费用
def sub_money(distance,count,month):
    info={} #声明字典
    money = 0
    sum = 0 #每个月的地铁费用
    global allcount #声明要修改全局变量
    allcount+=count*30  
    for i in range(0,count*30):
            if distance <= 6:
                    money = 3
            elif 6 < distance  and distance <= 12:
                    money = 4
            elif 12 < distance and distance <= 22:  
                    money = 5
            elif 22 < distance and distance <= 32:
                    money = 6
            elif distance > 32:
                    if(distance-32)%20 == 0:
                        money = 6 + (distance-32)/20
                    else:
                        money = 6 + int((distance-32)/20)+1
            if sum >=100 and sum < 150:
                    money = money*0.8
            elif sum >=150 and sum < 400:
                    money = money*0.5
            sum +=money
#计算总钱
def sum_money():
    sum = 0
    for i in list:
        for k,v in i.items():
            print("%d月份花费了%0.2f元"%(k,v))
            sum+=v
    return sum

#用户菜单输入
def user_input():
    loop = True
    while loop:
        mode = int(input("菜单 1:乘坐 2:计算\n"))
        if mode == 1:
            distance = float(input("请输入距离:"))
            month = int(input("请输入月份:"))
            count = int(input("请输入每天的次数:"))
            if month >= 13 or month <1:
                print("输入的不合法")
            elif count<=0:
                print("输入的不合法")
            else:
                sub_money(distance,count,month)
        else:
            result = sum_money()
            print("总共花了%0.2f元,一共花了%d次地铁"%(result,allcount))
            loop = False   #停止循环
user_input()
        




