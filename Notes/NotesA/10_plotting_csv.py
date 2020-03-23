import matplotlib.pyplot as plt
import csv

with open("Libraries_-_2019_Visitors_by_Location (1).csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(len(data))
headers = data.pop(0)
print(headers)

data.sort(key=lambda x: int(x[-1]))

library_names = [x[0] for x in data]
print(library_names)

monthly_data = [x[4:-1] for x in data]
print(monthly_data)

my_library = monthly_data[library_names.index('Lincoln Park')]
my_library = [int(x) for x in my_library]
print(my_library)

plt.figure(1)

