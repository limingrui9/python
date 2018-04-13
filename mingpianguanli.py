#名片管理系统
system = "欢迎进入名片管理系统"
print(system.center(50,"*"))
list = []
while True:
    card = int(input("请输入需要服务的项目1 添加 2 删除 3 修改 4 查询 5 退出"))
    if card == 1:#添加选项
        message = {}
        name = input("请输入姓名")
        age = int (input("请输入年龄"))
        work = input("请输入职位")
        email = input("请输入邮箱")
        tel = int(input("请输入电话"))
        isrepeat = False
        for info in list:
            for key in info:
                if info.get(key) == name:
                    print("用户已经存在，请从新输入")
                    isrepeat = True
                    break
        if not isrepeat:
            message["姓名"] = name 
            message["年龄"] = age
            message["职位"] = work
            message["邮箱"] = email
            message["电话"] = tel
            list.append(message)
            print("操作成功")
    
    elif card == 2:#删除选项
        delete = input("请选择要删除的用户")
        for i in list:
            if i ["姓名"] == delete:
                list.remove(i)
                print("操作成功")
            else:
                print("系统没有这个人")
    elif card == 3:#修改选项
        alter = input("请输入需要修改的用户名")
        for z in list:
        
                me = input("请输入要修改的项 1 姓名 2 年龄 3 职位 4 电话 5 退出")
                if me == "1":
                    my = input("请输入修改的名字:\t")
                    z["姓名"] = my
                    print("你已成功修改为: %s"%my)

                elif me == "2":
                    year = int(input("请输入需要更改的年龄:\t"))
                    z["年龄"] = year
                    print("你已成功修改年龄为 :%d"%year)
                elif me == "3":
                    job = input("请输入需要修改的职位")
                    z["职位"] = job
                    print("你已成功修改职位为 :%d"%job)
                elif me == "4":
                    number = int(input("请输入需要修改的电话:\t"))
                    z["电话"] = number
                    print("你已成功修改电话为: %d"%number)
                elif me == "5":
                    break
                else:
                    print("你的输入有误")
    elif card == 4:#查找选项
        find = input("请输入需要查找的用户:\t")
        for q in list:
            if q["姓名"] == find:
                for y in q:
                    print(y,q[y])
            else:
                    print("系统没有此人")
    elif card == 5:#退出程序
        break
    else:
        print("您的输入有误，请从新输入")


