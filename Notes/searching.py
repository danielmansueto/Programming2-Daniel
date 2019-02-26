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