# 11) Write a python script to store n lines in a file and displays the longest line in the file

# to open file in read mode
f=open('sample.txt','r')
# print max length of line from file
print(max(f))

f.close()