# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1, 101)]
# b) Make a list of even numbers from 20 to 40
my_even_list = [x for x in range(20, 41) if x ** 2 % 2 == 0]
my_even_list = [x for x in range(20, 41, 2)]
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_squares_list = [x ** 2 for x in range(1, 101)]
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_positives = [x for x in my_list if x > 0]

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
from Problems.number_list import *
print(num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
# Find and print the lowest number in num_list (1pt)
# Find and print the average of num_list (2pts)
# Remove the lowest number from num_list (2pt)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
print(max(num_list))
print(min(num_list))
print(sum(num_list)/len(num_list))
num_list.sort()
num_list.pop(0)
top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
freq_list = []
appearances = 0
number = 0
for n in num_list:
    if num_list.count(num_list, n) > appearances:
        appearances = my_list.count(num_list, n)
        number = n
print(number)

for num in num_list:
    freq = num_list.count(num)
    freq_list.append(freq)
freq_list.sort()
for num in num_list:
    if num_list.count(num) == 4:
        print(num)

# alternative with import
from statistics import mode
print(mode(num_list))

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
prime_num_list = num_list[:]
my_primes = []
for num in prime_num_list:
    for x in range(2, num):
        if (num % x) == 0:
            break
        else:
            if num not in my_primes:
                my_primes.append(num)
                print(num)

print(len(my_primes))

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for num in num_list:
    is_prime(num)
# Find the number of palindromes
# Hint: This may be easier to do with strings
palindrome = 0

for num in num_list:
    num = str(num)
    if num[0] == num[-1] and num[1] == num[-2]:
        palindrome += 1
print(palindrome)

def is_palindrome(my_string):
    for i in range(len(my_string)):
        if my_string[i] != my_string[-i - 1]:
            return False
    return True

