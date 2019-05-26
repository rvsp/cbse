# 9) Write a recursive code to display and calculate the sum of Geometric
# progression . a, ar, ar2 , ar3 , ar4 Up to n terms

# function to calculate sum of geometric series 
def sumOfGP(a, r, n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a * r 
        i = i + 1
    return sum
  
a = 1 # first term 
r = (float)(1/2.0) # common ratio 
n = 10 # number of terms 
          
print("value is : %.5f" %sumOfGP(a, r, n)), 