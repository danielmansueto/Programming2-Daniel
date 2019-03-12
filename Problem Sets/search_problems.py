'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

print()
print("Problem #1: ")
print()
length = []
dictionary = []

import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

with open('dictionary.txt') as f:
    dictionary = [x.strip().upper() for x in f]

for word in dictionary:
    number = len(word)
    length.append(number)

biggest = max(length)

lugar = length.index(biggest)
print("Longest word =", dictionary[lugar])
print()


#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

print("Problem #2:")
print()

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("AliceInWonderland.txt")
length = []
number = 0
average = 0

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        number += 1
        letter = len(word)
        length.append(letter)

sum = sum(length)
print("The average word length is", (sum / number), "letters")
print("The total word count is", number, "words")
print()

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

print("Problem #3:")
print()

file = open("AliceInWonderland.txt")
alice = []

for line in file:
    line = line.strip()
    words = split_line(line)
    for word in words:
        alice.append(word)

seven_letter = []
for i in alice:
    if len(i) == 7:
        seven_letter.append(i)
seven = []
for i in seven_letter:
    seven.append(seven_letter.count(i))

most = seven_letter[seven.index(max(seven))]
print("The most frequently occuring seven letter word is", most)


# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.


