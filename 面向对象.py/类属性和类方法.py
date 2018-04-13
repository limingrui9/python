class Tool(object):
    #使用赋值语句，定义类属性，记录创建工具的总数    
    count = 0

    def __init__(self,name):
        self.name = name
        Tool.count += 1

#创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")
#知道使用 Tool 类到底创建了多少个对象？
print("现在创建了%d个工具"% Tool.count)


