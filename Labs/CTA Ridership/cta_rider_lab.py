'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''

import matplotlib.pyplot as plt
import csv

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(data)

header = data.pop(0)
print(header)

data.sort(key=lambda x: int(x[0]))
last_10 = data[-11:]
years = [int(x[0]) for x in last_10]
rail = [int(x[3]) for x in last_10]
bus = [int(x[1]) for x in last_10]
total = [int(x[4]) for x in last_10]

plt.figure(1, tight_layout=True)
plt.plot(years, rail, color='blue', marker='*', label='Rail')
plt.plot(years, bus, color='black', marker='*', label='Bus')
plt.plot(years, total, color='red', marker='*', label='Total')
plt.xticks(years, rotation=45)
plt.xlabel('Years')
plt.ylabel('Ridership')
plt.title("CTA Ridership over the Past 10 Years", fontsize=18)
plt.legend()

plt.show()


# my hypothesis: ridership overall has gone down since the beginning/popularity of rideshare apps increase
# train ridership always lower than bus because of capacity reasons? they're pulling closer together not sure why



