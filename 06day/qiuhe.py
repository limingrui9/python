def _qiuhe():
    sum1 = 0#总和
    sum2 = 0#奇数和
    sum3 = 0#偶数和
    for i in range(0,101):
            if i%2 == 0:
                sum3 = sum3+i
            if i%2 != 0:
                sum2 = sum2+i

            sum1 =  sum1+i
    print(sum1)
    print(sum2)
    print(sum3)




_qiuhe()
