class LiMingRui(object):
    def wxx(self):

        import random
        a = random.randint(0,100)
        for i in range(1,a):
            r = int(input("请输入99以内的数字"))
            print("*"*50)
            if r > a:
                print("对不起,您猜大了哦")
            elif r < a:
                print("对不起，您猜小了哦")

            elif r == a:
                print("恭喜您猜对了哦")
                exit()
                print("结束游戏")
cao = LiMingRui()
cao.wxx()
