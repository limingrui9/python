class Tool(object):
    count = 0;
    def __init__(self,name):
        self.name = name
        Tool.count += 1
    @classmethod
    def tool_show_count(cls):
        print("创建了%d"%Tool.count)
        print("创建了%d"%cls.count)
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

Tool.tool_show_count()

'''
gai_zui = Tool("改锥")
luo_si_dao = Tool("螺丝刀")
'''

'''
print(Tool.count)
print(gai_zui.count)
print(luo_si_dao.count)
'''
