# Searching and read/write files

# forward slashgoes into a directory. ".." goes "up" a directory.
# by default, open( opens a file to read ('r')
file = open('../resources/super_villains.txt', 'r')
print(file)
file.close()  # ends your access to the file

# open a file to write with 'w'
# overwrites entire file

# open a file to append with 'a'
file = open('../resources/super_villains.txt', 'a')
file.write("\nMia the Horrible")  # wipe out entire file - overwrites
file.close()

# go through the info in the file line by line
file = open('../resources/super_villains.txt', 'r')
for line in file:
    print(line.strip().upper())  # take away spaces and make uppercase
file.close()  # ends your access to the file

# strip() method strips out spaces, tabs, returns
print("Hi\n".strip())
print("    Hello".strip())

# better way to open files (syntactic sugar)
with open('../resources/super_villains.txt') as f:  # by default opens to read  # f for file
    for line in f:
        print("Hello", line.strip().upper())

# read data into a list (array)
with open('../resources/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]  # adding text stripped and uppercase to list

print(villains)

# linear search
# python way
print("VARVARA TEMPEST" in villains)  # in keyword  # prints True

# brute force way
i = 0
key = "VARVARA TEMPEST"
while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < len(villains) - 1:
    print("Found", key, "at position", i)
else:
    print(key, "not found")

# make a function out of it!
def linear_search(key, my_list):
    """
    Searches for key inside of the list and returns True if you find it.
    :param key: item to find
    :param list: list to find key in
    :return: bool found
    """
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1

    if i < len(villains) - 1:
        print("Found", key, "at position", i)
        return True
    else:
        print(key, "not found")
        return False

print(linear_search("LAVINIA NYX", villains))

