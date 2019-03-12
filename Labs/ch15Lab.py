'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

print("Chapter 15 Lab:")
print()

import re
dictionary = []

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# Arraying the chapter
file = open('../Problem Sets/dictionary.txt')

for line in file:
    line = line.strip()
    dictionary.append(line)

file.close()

print('--- Linear Search ---')


file = open('AliceInWonderLand200.txt')
line_number = 0

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)
    for word in words:
        i = 0
        while i < (len(dictionary)) and word != dictionary[i]:
            i += 1
        if i >= len(dictionary):
            print('Found', word, 'misspelled at line', line_number)

file.close()

print('--- Binary Search ---')

file = open('AliceInWonderLand200.txt')
line_number = 0

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)
    for word in words:
        lower_bound = 0
        upper_bound = len(dictionary)
        found = False
        key = word.upper()

        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if dictionary[middle_pos] < key:
                lower_bound = middle_pos + 1
            elif dictionary[middle_pos] > key:
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print('Found', word, 'misspelled at line', line_number)

file.close()