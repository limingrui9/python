high = int(input("请输入你的身高"))
money = int(input("请输入你的身价"))
face = int(input("请输入你颜值分"))



if high>180 and money>1 and face>90:
    print("就可以是高富帅")
elif high<180 and money>1 and face>90:
    print("就可以是富帅") 
else:
    print("啦啦啦")
