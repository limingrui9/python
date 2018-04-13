try:
    num = int(input("请输入整数："))
    result = 8/num
    print(result)


except ValueError:

    print("输入正确的数")

except ZeroDivisionError:
    print("除0错误")

except Exception:
    print("有错误")

else:
    print("输入正确")


finally:
    print(".。。")
