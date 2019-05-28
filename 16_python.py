# 16) Write a python script to store name and telephone numbers in a text file and
# search for a specific name and change the telephone number of that name
# with new number. If the name is not found display error Message.

find = str(input('Enter name to find :'))
f = open('tele.txt','r')

new_val = None
for line in f:
    values = line.split()
    for li in values:
        if not li.isdigit():
            if li == find:
                new_num = input('Enter Number to change {}\'s :'.format(li))
                new_val ='\n' + li + ' ' + new_num
                break
        else:
            print('name not found')
            continue


fap = open('tele.txt','a')
fap.write(new_val)
fap.close()
