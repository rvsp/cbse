# 11) Write a python script to store n lines in a file and displays the longest line in the file


large_line = ''
large_line_len = 0
f = open('sample.txt', 'r')
for line in f:
    if large_line_len < len(line):
        large_line_len = len(line)
        large_line = line

print(large_line)
