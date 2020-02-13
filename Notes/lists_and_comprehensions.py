# LISTS
import random

my_names = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo"]
my_numbers = [5, 9, 12, 6, -3, 6]

# indexing lists
print(my_names)
print(my_names[2])  # Cam
print(my_names[-1])  # Flo
print(my_names[:3])  # Abe to Cam
print(my_names[3:5])  # Dan and Eve (doesn't include 3)
print(my_names[:])  # Everybody

# copy a list
my_copy = my_names  # No!!! Stop it! not really a copy, we're talking to the same list
my_copy.append("Gil")
print(my_copy)
print(my_names)
my_copy = my_names[:]  # generates a new list so copy "points" at it's own thing
my_names.append("Hal")
my_copy.append("Hor")
print(my_copy)
print(my_names)

#2D Lists
my_2d = [["peanut", "butter", "jelly","time"],["Hey", "Ya", "Hey", "Ya"], ["With a", "Baseball", "Bat"]]
print(my_2d[1])  # ["Hey", "Ya", "Hey", "Ya"]
print(my_2d[1][1])  # Ya
my_2d[1].append("OutKast")
print(my_2d)

# if in
if "Hal" in my_names:
    print("Hal is in my_names")

# LIST FUNCTIONS
print(len(my_names))  # length of the list (not the last index!), will spit out last list item + 1
print(min(my_numbers))  # lowest value
print(max(my_numbers))  # highest value
print(sum(my_numbers))  # add em up, bobby, add em up

print(min(my_names))  # first in alphabetical order
my_names.append("Aaron")
print(min(my_names))  # will still be Abe because you added it first, lowercase don't come until 9

# LIST METHODS
print(my_names.index("Cam"))  # returns the index of "Cam"  # will be 2
my_names.append("Cam")
print(my_names.index("Cam"))  # only sees the fist instance, still return 2
print(my_names.count("Cam"))  # occurs twice
print(my_names.count("Mia"))  # occurs zero times :(


print(my_names.append("Ice"))
print(my_names.append("Cic"))
print(my_names)
del my_names[my_names.index("Aaron")]
print(my_names)
my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)

# MODIFYING LISTSpop
del my_names[10]
print(my_names)

my_names.pop()  # pops one off the end of the list
print(my_names)
end_of_list = my_names.pop() # pops off end AND RETURNS IT
print(my_names)
print(end_of_list)

front_of_list = my_names.pop(0) # pop by index
print(front_of_list)
print(my_names)

# concatenation
first = "Francis"
last = "Parker"
print(first + last)  # smooshes them together
print(my_names + my_numbers) # one big list

# ITERATING THROUGH LISTS
# make a list of numbers 0 through 9
# make empty list, make for loop, append the index to the for loop

my_loop_list = []
for i in range(10):
    my_loop_list.append(i)

print(my_loop_list)

# print every item in the list you just created
for item in my_loop_list:
    item += 1
    print(item)

print(my_loop_list)  # didn't actually change the list in the for loop bc you didn't return

# add one to every item in the list (use an INDEX variable loop)
for i in range(len(my_loop_list)):
    my_loop_list[i] += 1

print(my_loop_list)

# SAMPLE LIST COMPREHENSION
my_loop_list = [x for x in range(10)]
print(my_loop_list)

# list comprehension
my_list = []

for i in range(101):
    my_list.append(i)

print(my_list)

#  using list comprehension

my_list = [x for x in range(101)]
print(my_list)

print()

for i in range(101):
    my_list.append(i ** 2)
print(my_list)

my_list = [x ** 2 for x in range(101)]
print(my_list)

#  make the same list but filter out the odd
my_list = []
for i in range(101):
    if i ** 2 % 2 == 0:
        my_list.append(i ** 2)

print(my_list)

my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]
print(my_list)

#  roll a single die 100 times and add it to the list
my_list = []

for i in range(100):
    my_list.append(random.randrange(1, 7))

print(my_list)

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)

# roll two dice
my_list = []

for i in range(100):
    my_list.append([random.randrange(1, 7), random.randrange(1, 7)])

print(my_list)

my_list = [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)]
print(my_list)

# go back through it and sum

my_sums = [sum(x) for x in my_list]
print(my_sums)

# hundred rolls but only the doubles

my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)
print(len(my_doubles))

# all at once: roll a hundred pairs and only add doubles

my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)] if x[0] == x[1]]
print(my_list)

# Working with Strings is a lot like lists
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first + last)
print(last[-2:])

for letter in first:
    print(letter)

if "N" in first:
    print("YES")

