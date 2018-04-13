def sum (a,b):
    def sum1(c):
        return a+b+c


    return sum1


result = sum(1,2)
name = result(9)
print(name)
