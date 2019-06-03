''' 12) Write a python script to store roll no, name and marks in 3 subjects of
 students in a class in file marks.txt, append the file with 2 more records,
 display the contents.
'''

def add3Record():
    f = open('marks.txt', 'w+')
    for i in range(3):
        rollno = str(input('rollno: '))
        name = str(input('name: '))
        li = []
        for j in range(3):
            li.append(str(input('mark: ')))
        temp = rollno + ' ' + name
        z = ''
        for lis in li:
            z = z + ' ' + lis
        temp = temp + z + '\n'
        f.write(temp)
        print('temp', temp)

def append2Record():
    f = open('marks.txt', 'a+')
    for i in range(2):
        rollno = str(input('rollno: '))
        name = str(input('name: '))
        li = []
        for j in range(3):
            li.append(str(input('mark: ')))
        temp = rollno + ' ' + name
        z = ''
        for lis in li:
            z = z + ' ' + lis
        temp = temp + z + '\n'
        f.write(temp)
        print('temp', temp)

def display():
    f=open('marks.txt','r')
    print(f.read())

value = input('choice to create & append values in file\n 1.add three record\n 2.append two more record\n 3.display content\n')
if value==1:
    add3Record()
elif value ==2:
    append2Record()
elif value ==3:
    display()