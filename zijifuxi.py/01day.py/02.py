#小明
'''
name = "小明"
print("我的名字叫%s请多多关照"%name)
student_no = 1
print("我的学号是%06d"%student_no)
'''
#买西瓜
'''
prince = 9
weight = 5
money = prince*weight

print("西瓜%.2f元一斤  购买了%.2f斤  一共花了%.2f元"%(prince,weight, money))
'''
#王者
'''
age = int(input("请输入年龄"))


if age<4:
    print("王者是啥")
else:
    print("王者是游戏")
'''
'''
#年份
year = int(input("请输入一个年份"))

if year>0:
    if year%4 == 0 and year%100 != 0:
        print("闰年")
    elif year %400 == 0:
        print("闰年")
    else:
        print("平年")
else:
    print("你输入的年份不合法")
'''















