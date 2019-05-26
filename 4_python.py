# 4) Using recursive function find factorial of a natural number

# recursive function to calculate
def recursive(n):
   if n == 1:
       return n
   else:
       return n*recursive(n-1)

# Change this value for a different result
num = int(input('Enter natural number for factorial calculation : '))

# check is the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of {} is {}".format(num,recursive(num)))