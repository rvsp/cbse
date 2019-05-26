# 14) Write a python to read characters from the keyboard one by one all lower
# case characters get stored in the file lower.txt all upper case characters
# get stored in the file upper.txt and all other characters get stored in 
# others.txt. display content of all files.
value = raw_input('enter value')
for s in value:
    if s.isupper():
        fupper = open('upper.txt','a+')
        fupper.write(s)
        fupper.close()
    elif s.islower():
        flower = open('lower.txt','a+')
        flower.write(s)
        flower.close()
    else:
        fothers = open('others.txt','a+')
        fothers.write(s)
        fothers.close()


flowerContent = open('lower.txt','a+')
print('content from lower.txt file {} : '.format(flowerContent.read()))
fupperContent = open('upper.txt','a+')
print('content from upper.txt file {} : '.format(fupperContent.read()))
fothersContent = open('others.txt','a+')
print('content from others.txt file {} : '.format(fothersContent.read()))