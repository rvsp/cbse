# 7) Write a recursive code to test string is palindrome or not

# function to check given string is palindrome
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

# to get string as input 
a=raw_input("Enter string to check palindrome:")

if(is_palindrome(str(a))==True):
    print("{} : String is a palindrome!".format(a))
else:
    print("{} : String isn't a palindrome!".format(a))