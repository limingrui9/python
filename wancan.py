str = "晚餐系统"
print(str.center(50,"*"))

list = []

#加入
for i in range(4):
    name = input("请输入姓名")
    list.append(name)

#打印
for i in list:
    print("吃饭吧%s"%i)
#无法赴约的人
print("无法赴约的人%s"%list.pop())
name = input("请输入新的客人")
list.append(name)

#新的赴约名单
for i in list:
    print("新的赴约名单%s"%i)

#用pop删除
for i in list:
    list.pop()
    if len(list) == 2:
        break

for i in list:
    print("两个人的晚餐%s"%i)







