'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dic_file = open('dictionary.txt', 'r')
dictionary_list = []
for word in dic_file:
    dictionary_list.append(word.strip())
dic_file.close()

alice_wonderland_file = open('AliceInWonderLand.txt', 'r')

# functions
def linear_search(key, my_list, line_num):
    """
    :param key: what you are looking for
    :param list: where you are looking
    :return: bool did you find it?
    """
    i = 0
    while i < len(my_list) and key.upper() != my_list[i]:
        i += 1
    if i < len(my_list):
        return True
    else:
        print(key, "at line", line_num, "is not in the dictionary.")
        return False

def binary_search(key, my_list, line_num, list_type):
    lower_bound = 0
    upper_bound = len(my_list)
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        return True
    else:
        print(key, "at line", line_num, "is not in", list_type)
        return False


# linear search
line_number = 0
print("--- Linear Search ---")
for line in alice_wonderland_file:
    line = line.strip().upper()
    words = split_line(line)
    line_number += 1
    for word in words:
        dictionary_vs_alice = linear_search(word, dictionary_list, line_number)

alice_wonderland_file.close()

# binary_search
alice_wonderland_file = open('AliceInWonderLand.txt', 'r')

print("--- Binary Search ---")
line_number = 0
for line in alice_wonderland_file:
    line_number += 1
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        dictionary_vs_alice = binary_search(word, dictionary_list, line_number, "the dictionary.")

alice_wonderland_file.close()

# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
print("---Challenge Problem ---")
alice_wonderland_file = open('AliceInWonderLand.txt', 'r')
alice_list = []
for word in alice_wonderland_file:
    word.upper()
    alice_list.append(word)

print(alice_list)
alice_wonderland_file.close()

lookingglass_file = open('AliceThroughTheLookingGlass.txt', 'r')
print("--- Binary Search ---")
line_number = 0
for line in lookingglass_file:
    line_number += 1
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_vs_alice = binary_search(word, alice_list, line_number, "Alice Through the Looking Glass.")

alice_wonderland_file.close()





