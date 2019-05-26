''' 10. write a program to
1) create a text file
2) display content of file
3) display line count of the file
4) display the word count of the file
5) display character count of file
'''
fname = input("Enter the name of the file:")
infile = open(fname, 'r+')
lines = 0
words = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print('line count of the file : {}'.format(lines))
print('word count of the file : {}'.format(words))
print('character count of file : {}'.format(characters))
print('content of file below : ',infile.readline())
# file close
infile.close()