'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re
from typing import List


def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
length = 0
winner_word = 0
dictionary_file = open('dictionary.txt', 'r')
for word in dictionary_file:
    if len(word) >= length:
        length = len(word)
        winner_word = word

print(winner_word)

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
total_count = 0
total_length = []
alice_file = open('AliceInWonderLand.txt', 'r')
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        total_count += 1
        total_length.append(len(word))
average_length = sum(total_length) / len(total_length)


print("The total word count is", total_count, ".")
print("The average length of a word in Alice in Wonderland is", average_length, "letters.")


# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_count = []

alice_file = open('AliceInWonderLand.txt', 'r')
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_count.append(word)

print(alice_count.count("ALICE") + alice_count.count("ALICE'S"))

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_freq = 0
seven_winner = 0
alice_file = open('AliceInWonderLand.txt', 'r')
for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if len(word) == 7:
            if alice_count.count(word) >= seven_freq:
                    seven_freq = alice_count.count(word)
                    seven_winner = word
print(seven_winner)

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

cheshire_cat = 0
next_word = 0
print("Cheshire occurs", alice_count.count("CHESHIRE"), "times.")
print("Cat occurs", alice_count.count("CAT"), "times.")

for word in alice_count:
    if word == "CHESHIRE":
        print(word)
        next_word = alice_count.index(word)
        print(alice_count[next_word + 1])
        if alice_count[next_word + 1] == "CAT":
            cheshire_cat += 1
            
print(cheshire_cat)



