'''
3) A menu driven program using functions 
a. To sum all prime numbers up to n
b. To sum all 3 digits Armstrong numbers 
c. To sum all perfect numbers from 100 to 1000
'''

def calSumOfPrime(r):
    sum=0
    for a in range(2,r+1):
        k=0
        for i in range(2,a//2+1):
            if(a%i==0):
                k=k+1
        if(k<=0):
            sum+=a
    print('sum of all prime numbers up to n',sum)

# to get input from user
value = int(input('Enter option : '))
# a. To sum all prime numbers up to n
if value==1:
    calSumOfPrime(int(input("Enter value to sum : ")))