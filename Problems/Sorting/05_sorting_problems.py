
'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import *
#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
header = data.pop(0)
print(header)
# print(header[2])
'''

['', 'Year', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 
'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'blanl', 'OWS', 'DWS', 'WS', 
'WS/48', 'blank2', 'OBPM', 'DBPM', 'BPM', 'VORP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', 
'2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
'''

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)

data.sort(key=lambda a: a[-1])

new_list = data[-10:]
for player in new_list:
    print(player[2])

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
career_points = 0
for player in data:
    if player[2] == "Kobe Bryant":
        career_points += player[-1]

print("Kobe Bryant had", career_points, "career points.")

#4  What player has the most 3point field goals in a single season. (3pts)
data.sort(key=lambda a: a[-19])
print(data[-1][2])

#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time?

data.sort(key=lambda a: a[-28])
print(data[-1][2], "had the highest WS/48 season of all time.")

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".

# Who is the youngest player of all time?
data.sort(key=lambda a: a[5])
print(data[0][2], "was the youngest player of all time.")

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
data.sort(key=lambda a: a[-1])
challenge_list = data[-100:]
challenge_list.sort(key=lambda a: a[-10])
print("Worst free throw percentage is", challenge_list[0][2])
print("Best free throw percentage is", challenge_list[-1][2])


