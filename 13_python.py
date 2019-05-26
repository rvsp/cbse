# 13) Write a python script to copy a text files source.txt into another file target.txt
# except the lines starting with '@'

with open('source.txt') as fsource:
    with open("target.txt", "w") as fdest:
        for line in fsource:
            if not line.startswith('@'):
                fdest.write(line)  

fsource.close()
fdest.close()