# Searching

# use forward slashes to go into folders and .. to go "up" a folder
file = open('../resources/super_villains.txt', 'r')  # open to read
print(file)

for line in file:
    print(line.strip())

file.close()

# .strip() method removes the extra characters at end of text
print("    Hello ".strip())
print("World\n".strip())
print("!")

# 'w' opens to write and overwrites the file
# 'a' opens to append
file = open('../resources/super_villains.txt', 'a')
file.write('Lee the Merciless\n')
file.write('Rohan the Destroyer\n')
file.close()

# open to write can create a new file
file = open('../resources/heroes.txt', 'w')
file.write('Owen the Valiant\n')
file.close()

#  Better way to open close a file (syntactic sugar)
# file automatically closes after execution of with
with open('../resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())


# .read() method just imports whole file as a string
with open('../resources/super_villains.txt') as f:
    read_data = f.read()  # big string

print("\n\nRead method")
print(read_data)

# Reading data into an array (list)
with open('../resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# Linear Search (not very efficient but easy)

key = "Vidar the Manic".upper()

i = 0
while i < (len(villains)) and key != villains[i]:
    i += 1

if i < len(villains):
    print("Found it at position", i)
else:
    print(key, "is not in the list")

# try to make this into a function

def linear_search(key, list):
    """
    :param key: what you are looking for
    :param list: where you are looking
    :return: bool did you find it?
    """





