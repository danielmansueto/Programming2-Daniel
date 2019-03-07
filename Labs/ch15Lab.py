'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

file = open("../Problem Sets/dictionary.txt")

dictionary = []
for line in file:
    line = line.strip()
    dictionary.append(line)

file.close()
file = open('../Problem Sets/AliceInWonderLand.txt')
line_number = 0

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)


import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

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