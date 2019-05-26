# Write a python script using os module:
#   (1) To display current working directory
#   (2) To display the content of a directory
#   (3) Create a new directory called Mydir
#   (4) To change the current working directory to Mydir
#   (5) Store a text file test.txt
#   (6) Rename the file test.txt to exam.txt
#   (7) To remove exam.txt if exists otherwise display error Message
#   (8) To change the Mydir to Yourdir
#   (9) To Exit

import os

while True:
    print('(1) To display current working directory\n(2) To display the content of a directory\n(3) Create a new directory called Mydir\n(4) To change the current working directory to Mydir\n(5) Store a text file test.txt\n(6) Rename the file  test.txt to exam.txt\n(7) To remove exam.txt if exists otherwise display error Message\n(8) To change the Mydir to Yourdir\n(9) Exit')
    choice = int(input('Enter choice : '))
    temp = os.getcwd()
    if choice ==1:
        print('current working directory',os.getcwd())
    elif choice ==2:
        print('content of a directory',os.listdir(temp))
    elif choice == 3:
        os.mkdir('Mydir')
        print('to list newly created dirctory', os.listdir(temp))
    elif choice == 4:
        os.chdir('Mydir')
        print('content of changed directory',os.getcwd())
    elif choice == 5:
        print('Store a text fil`e test.txt',os.getcwd())
        f = open('test.txt','w+')
    elif choice ==6:
        print('Rename the file test.txt to exam.txt')
        os.rename('test.txt','exam.txt')
    elif choice == 7:
        try:
            os.remove('exam.txt')
            print('exam.txt file deleted successfully')
        except:
            print('No such file or directory')
    elif choice == 8:
        os.rename('Mydir','Yourdir')
        print(os.listdir())
    elif choice == 9:
        print('Thanks, Bye!')
        exit()