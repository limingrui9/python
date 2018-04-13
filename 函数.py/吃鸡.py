import time
def kill():
    for i in range(1,9):
        time.sleep(2)
        if i == 6:
            print("游戏结束了")
            break
        else:
            print("杀了%d"%i)




def play():
    print("开始捡东西")
    kill()


def login(token):
    if token == "159159":
        print("登录成功")
        play()




def saoyisao(token):
        print("开始扫一扫") 
        login(token)



saoyisao("159159")
