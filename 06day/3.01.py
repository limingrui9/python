def addUser():
    list = []
    while True:
            info = {}
            name = input("请输入名字")
            age = input("请输入年龄")
            if not list:
                    info["name"] = name
                    info["age"] = age
                    list.append(info)
            else:
                    isrepeat = False
                    for i in list:
                            for k,v in i.items():
                                    if v == name:
                                            print("你输入重复了")
                                            isrepeat = true
                                            break


                    if not isrepeat:
                            info["name"] = name
                            info["age"] = age
                            list.append(info)
            for i in list:
                    print(i)


addUser()
