# searching (chapter 15 from programarcadegames.com)

file = open('imports/super_villains.txt', 'r')  # open file to read
print(file)

for line in file:
    print("Hello", line.strip())  # you can only read through one time

file.close()  # ends your access to file


# open a file to write (overwrites all previous)
'''
file = open('imports/super_villains.txt', 'w')  # open file to write
file.write('Lee the Merciless\n')
file.close()

file = open('imports/super_villains.txt', 'r')  # open file to read
for line in file:
    print(line.strip())  # strip method removes any extra spaces, /t, /n
file.close()
'''

# open a file to append (does not overwrite)
file = open('imports/super_villains.txt', 'a')  # open file to append
file.write('Dan the Man\n')
file.close()

file = open('imports/super_villains.txt', 'r')  # open file to read
print()
for line in file:
    print(line.strip())  # strip method removes any extra spaces, \t, \n
file.close()

# you can make a new file by opening to write
file = open('imports/oscars.txt', 'w')
file.write('Green Book\tBest Picture\t')
file.close()

# better way to open and close a file

with open('Imports/super_villains.txt') as f:
    for line in f:
        print(line.strip())
    read_data = f.read()  # big string

# file automatically closes from with statement
print(read_data)

# read data into a list (array)
with open('Imports/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]
print(villains)

# linear search
print(villains.index("RENARD THE TORTURER"))

key = "RENARD THE TORTURER"  # what we are looking for
i = 0  # index of my search

while i < len(villains) and key != villains[i]:
     i += 1

if i < len(villains):
    print("Found", key, "at position", i)
else:
    print("Could not find", key)

# binary search
villains.sort()

key = "THEODORA THE WICKED"
lower_bound = 0
upper_bound = len(villains)
found = False
loops = 0

# loop until we find it (or we go through the entire list)
while lower_bound <= upper_bound and not found:
    loops += 1
    middle_pos = (upper_bound + lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print(key, "was found at position", middle_pos)
else:
    print(key, "was not found after", loops, "loops")

import re

text = "Hello my name is Alexa"

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

line = split_line(text)
print(line)

file = open("Imports/super_villains.txt")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        print(word)