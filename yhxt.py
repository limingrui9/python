account = "lmr"
passwd = "123123"

myaccount = input("请输入一个账号")
mypasswd = input("请输入一个密码")


if myaccount == account  and   mypasswd == passwd:
    print ("您输入的密码正确")
    myif =input ("请输入存钱，1  取钱，2")
    if myif == "1":
        print("i")
    elif myif == "2":
        print("")
    else:
        print("您输入错误呀")





else:
    print("对不起，你输入的密码有误")
