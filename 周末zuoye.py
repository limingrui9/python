'''
#第一题
for i in range(1,5001):#格式  1-5001是范围
    if (i%5==0 and i%7==0):#括号里面的是条件
        print(i)#输出i（i可以随便自己起，他就是一个名字）
'''
'''
#第二题
import random#导入一个随机数
computer = random.randint(1,100)#给电脑赋值，（1,100）
for i in range(1,11):#格式，循环数，循环10次
    me = int(input("请输入一个数字"))#输入一个数字是内容
    if me > computer:#如果自己的大于电脑
        print ("您输入的数字大了，请从新输入")#就从新输入
    elif me < computer:#如果小于电脑
        print ("您输入的数字小了，请从新输入")#从新输入
    else:#否则
        print ("您输入的对咯")#就对了
        break#跳出循环体
'''
'''
#第三题
username = "lmr"
passwd = 123456
mysuername = input("请输入账号")
mypasswd = int(input("请输入密码"))
if(mysuername == username and mypasswd == passwd):
    print("欢迎进去李明瑞的世界")
else:
    print("密码或用户名错误")
'''
'''
#第四题
count = 1
while count <=9:
    if count<=5:
        print("*"*count)
    elif count>5:
        print("*"*(10-count))

    count+=1
'''
#第五题
for i in range(2,101):
    if(i==2 or i==3 or i==5 or i==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
        print(i)

