# 2) Program to sum the series using user defined function
# 1+1/1!-2/2!+3/3!-4/4!+......+-n/n!

def fact(num):
    fact =1
    i = 1
    for i in range(num):
        fact = fact*i
    return fact/num


def calculate():
    value = int(input('Enter Value :'))
    sum = 1.0
    i = 1
    for i in range(value):
        if i % 2 == 0:
            sum = sum - fact(i)
        else:
            sum = sum+fact(i)
    print('calculated value', sum)


calculate()
