import matplotlib.pyplot as plt
import csv
import numpy as np

# read in data file
with open("Final/top10s.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

# get header
header = data.pop(0)
print(header)

# sort by popularity
data.sort(key=lambda x: int(x[-1]))

# get rid of popularity outliers
for song in data:
    if int(song[-1]) < 50:
        data.pop(data.index(song))

# lists for key years
ten = []
nineteen = []

for song in data:
    if song[4] == '2010':
        ten.append(song)
    if song[4] == '2019':
        nineteen.append(song)

# popularity, duration, and song titles by year
alltime = [int(x[7]) for x in data]
alltime.sort()
print(alltime)
popularity_ten = [int(x[-1]) for x in ten]
popularity_nineteen = [int(x[-1]) for x in nineteen]
acousticness_ten = [int(x[-3]) for x in ten]
acousticness_nineteen = [int(x[-3]) for x in nineteen]
danceability_ten = [int(x[7]) for x in ten]
danceability_nineteen = [int(x[7]) for x in nineteen]
song_title_ten = [str(x[1]) for x in ten]
song_title_nineteen = [str(x[1]) for x in nineteen]
duration_ten = [int(x[-4]) for x in ten]
duration_nineteen = [int(x[-4]) for x in nineteen]

# top genres by year
all_genres = [x[3] for x in data]
genre_ten = [x[3] for x in ten]
genre_nineteen = [x[3] for x in nineteen]
genre_ten_count = []
genre_nineteen_count = []
all_genres_count = []

# definitions for counting
def Remove(duplicate):  # found on stack overflow
    final_list = []
    for genre in duplicate:
        if genre not in final_list:
            final_list.append(genre)
    return final_list


def genre_count(year_list, count_list):
    for genre in year_list:
        count_list.append([year_list.count(genre), genre])
    count_list.sort(key=lambda x: x[0])
    return count_list

# running count on lists
genre_count(genre_ten, genre_ten_count)
genre_ten_count = Remove(genre_ten_count)
genre_count(genre_nineteen, genre_nineteen_count)
genre_nineteen_count = Remove(genre_nineteen_count)
genre_count(all_genres, all_genres_count)
all_genres_count = Remove(all_genres_count)
print(all_genres_count)


# GRAPHS START HERE
# FIGURE ZERO - popularity vs. acousticness
plt.figure("Popularity vs. Acousticness", figsize=(10, 6))

# two scatters - 2010 and 2019
plt.scatter(popularity_ten, acousticness_ten, color='#65c7c5')
plt.scatter(popularity_nineteen, acousticness_nineteen, color='#fc6869')

# labels, title
plt.xlabel("Popularity (out of 100)")
plt.ylabel("Acousticness (out of 100)")
plt.title("Popularity vs. Acousticness", fontsize=20)

# best fit
p = np.polyfit(popularity_ten, acousticness_ten, 1)  # best fit 2010
p2 = np.polyfit(popularity_nineteen, acousticness_nineteen, 1)  # best fit 2010

x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]  # linear 1st order
plt.plot(x, y)

# annotate song titles
for i in range(len(song_title_ten)):
    plt.annotate(song_title_ten[i], xy=(popularity_ten[i], acousticness_ten[i]), fontsize=5)

for i in range(len(song_title_nineteen)):
    plt.annotate(song_title_nineteen[i], xy=(popularity_nineteen[i], acousticness_nineteen[i]), fontsize=5)

# figure one - popularity vs. danceability
plt.figure("Popularity vs. Danceability", figsize=(10, 6))

# two scatters - 2010 and 2019
plt.scatter(popularity_ten, danceability_ten, color='#65c7c5')
plt.scatter(popularity_nineteen, danceability_nineteen, color='#fc6869')

# labels, title
plt.xlabel("Popularity (out of 100)")
plt.ylabel("Danceability (out of 100)")
plt.title("Popularity vs. Danceability", fontsize=20)

# best fit
p = np.polyfit(popularity_ten, danceability_ten, 1)  # best fit 2010
p2 = np.polyfit(popularity_nineteen, danceability_nineteen, 1)  # best fit 2010

x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]  # linear 1st order
plt.plot(x, y)

# annotate song titles
for i in range(len(song_title_ten)):
    plt.annotate(song_title_ten[i], xy=(popularity_ten[i], danceability_ten[i]), fontsize=5)

for i in range(len(song_title_nineteen)):
    plt.annotate(song_title_nineteen[i], xy=(popularity_nineteen[i], danceability_nineteen[i]), fontsize=5)

# FIGURE TWO - popularity vs duration
plt.figure("Popularity vs. Duration", figsize=(10, 6))

# two scatters - 2010 and 2019
plt.scatter(popularity_ten, duration_ten, color='#65c7c5')
plt.scatter(popularity_nineteen, duration_nineteen, color='#fc6869')

# best fit
p = np.polyfit(popularity_ten, duration_ten, 1)  # best fit 2010
p2 = np.polyfit(popularity_nineteen, duration_nineteen, 1)  # best fit 2010

x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]  # linear 1st order
plt.plot(x, y)

# annotate song titles
for i in range(len(song_title_ten)):
    plt.annotate(song_title_ten[i], xy=(popularity_ten[i], duration_ten[i]), fontsize=5)
for i in range(len(song_title_nineteen)):
    plt.annotate(song_title_nineteen[i], xy=(popularity_nineteen[i], duration_nineteen[i]), fontsize=5)

# labels and title
plt.xlabel("Popularity (out of 100)")
plt.ylabel("Duration (out of 100)")
plt.title("Popularity vs. Duration", fontsize=20)

# FIGURE THREE - bar graph of popular genres 2010 vs. 2019 (with help from stack overflow)
plt.figure("Bar Graph", figsize=(10, 6))

genres_list = [str(x[1]) for x in genre_ten_count]
y_pos = np.arange(len(genres_list))
counts = [int(x[0]) for x in genre_ten_count]

plt.bar(y_pos, counts, align='center', color='#65c7c5')
plt.xticks(y_pos, genres_list, fontsize=6)
plt.ylabel('Appearances')
plt.xlabel('Genres')

plt.title('Top Genres 2010 vs. 2019')

'''

genres_list_19 = [str(x[1]) for x in genre_nineteen_count]
y_pos_19 = np.arange(len(genres_list_19))
counts_19 = [int(x[0]) for x in genre_nineteen_count]

plt.bar(y_pos_19, counts_19, align='center', color='#fc6869')
plt.xticks(y_pos_19, genres_list_19)
plt.ylabel('Appearances')
plt.xlabel('Genres')
'''

plt.show()


