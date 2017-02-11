import re

count=0
#reading text file
file = open('FirstAssignment.txt')
for line in file:
    line.rstrip()
    list_file = re.findall('([0-9]+)',line)

    for x in list_file:
        count += int(x)
print count
