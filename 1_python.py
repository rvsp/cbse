# def splitNum(n):
#     if n < 10:
#         return [n]
#     else:
#         return splitNum(n // 10) + [n % 10]

# print(splitNum(1233))


a,b = divmod(1233,10)
print('a,b',a,b)