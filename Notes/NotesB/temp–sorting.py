# Sorting
import random
import time

# swap values
a = 1
b = 2

temp = a
a = b
b = temp
print(a, b)

# pythonic way
a, b = b, a  # works only in python
print(a, b)

# make a random list of 100 numbers with values 1 to 99
my_list = [random.randrange(1, 100) for x in range(1000)]
my_list2 = my_list[:]
print(my_list)

for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

print(my_list)

# INSERTION SORT

for key_pos in range(1, len(my_list2)):
    key_val = my_list2[key_pos]  # key dancer
    scan_pos = key_pos - 1  # look to the dancer's left
    while scan_pos >= 0 and key_val < my_list2[scan_pos]:
        my_list2[scan_pos + 1] = my_list2[scan_pos] # move the scan position left
        scan_pos -= 1
    my_list2[scan_pos + 1] = key_val # commit the move

print(my_list2)

# optional function parameters
print("Hello", end=" ")
print("Mom", end="!\n")
print("Hello", "Mom", sep="Your", end="!!!") # default sep is space

def hello(name, time_of_day):
    print("Hello", name, "good", time_of_day)

hello("Mr. Lee", "afternoon")
hello("Mia", time_of_day="afternoon")
hello("Star", time_of_day="evening")


# file opening (IOError, FileNotFoundError)
try:
    file = open("AliceInWonderland.txt")
except:
    print("Could not open file.")

# Use built in error types for python to check what error occured.
try:
    # my_file = open("myfile.txt")
    int("Hello")
except FileNotFoundError:
    print("File not found.")
except ValueError as e:
    print("Invalid conversion")
    print(e)
except ZeroDivisionError as e:
    print("Error:", e)

# Formatting Numbers
import random

# round function round(n, digits)
print(round(3.1415926, 2))

# format method (string method)
a  = 6969696969
b = 420.42069
print("My number is {}".format(a))  # {} is the formatted number
print("My number is {:.3f}".format(b))
print("My numbers are {} and {}".format(a, b))  # places them sequentially unless otherwise specified
print("My numbers are {1:} and {0}".format(a, b))  #otherwise specified
print("My numbers are {1: .3f} and {0}:,".format(a, b))  #otherwise specified

# fixed width
for i in range(20):
    c = random.randrange(10000)
    print("${:4}".format(c))

# justification ^ center <left >right
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:^12}dollars".format(c))

# add commas
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:12,}".format(c))

  # precision (f float, d dec/int,
for i in range(20):
    c = random.random()
    print("{:<11.5f}".format(c))
