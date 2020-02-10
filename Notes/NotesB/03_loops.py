# More on LOOPS

# Basic FOR loop
import random

for i in range(5, 51, 5):
    print(i, end="")
print()
# RANGE function (alternative for comprehension)
my_list = list(range(100))  # iterable
print(my_list)

# BREAK
for number in my_list:
    if number > 10:
        break
    print(number, end=" ")

print("End of loop")

# CONTINUE (skips to the end of the loop for that iteration)
for number in my_list:
    if number % 7 == 0:
        continue  # skips the rest of this iteration
    print(number, end=" ")

# FOR ELSE
for number in my_list:
    if number == 200:
        print("You unnaturally finished the loop")
        break
    print(number)
else:
    print("You naturally finished the loop.")



# Add me as a collaborator on Github


