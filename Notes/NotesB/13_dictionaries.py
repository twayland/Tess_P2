# dictionaries (dict)

# list, tupkle, int, float, bool, str, set, dict

# sets (not generally used often)
# a unique list of items (no repeats)
# uses {} instead of []

my_set = {1, 2, 3, 4, 4, 5}
print(my_set) # the extra 4 will ddrop

my_list = ['milk', 'toilet paper', 'yeast', 'strawberries', 'milk']
print(set(my_list))

# get rid of duplicates
my_list = list(set(my_list))
print(my_list)
print(type(my_list))

# dictionaries
lee1 = ['Aaron', 46, 'English', 'Python']
mr_lee = {'first name': 'Aaron', 'age': 46, 'spoken language': ['English', 'Pig Latin'], 'fav prog lang': 'Python'}
the_office = {'title': 'The Office',
              'genre': ['Mockumentary', 'Sitcom'],
              'developedBy': 'Greg Daniels',
              'starring': ['Steve Carell', 'Rainn Wilson', 'John Krasinski', 'Jenna Fisher']}

# acess a dict
print(the_office['genre'])
# print(the_office[0]) # produces error, keyerror

# add to a dictionary
the_office['# seasons'] = 9

# change value
the_office['# seasons'] += 1

# add to values
the_office['starring'].append("Mindy Kaling")

# what are my keys?
print(the_office.keys())
print(the_office.values())

# next show
parks_rec = {'title': 'Parks and Recreation', 'created by': ['Greg Daniels', 'Michael Schur']}
shows = [the_office, parks_rec]

for key in the_office:
    print(key)  # prints the keys
    print(the_office[key]) # prints values

