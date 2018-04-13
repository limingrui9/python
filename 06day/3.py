

def _zidian():
    title="***"
    print(title.center(20,"*"))
    list=[]
    dic={}

    name = input("请输入名字")
    year = int(input("请输入年龄"))
    dic["name"]=name
    dic["year"]=year
    list.append(dic)
    print(list)
    for i in list:
        for k,v in i.items():
            print(k,v)
_zidian()
_zidian()
