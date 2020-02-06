# Hangman game

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

# tips
# use .UPPER or.lower


gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

import random
word_list = ["Iowa", "Sanders", "Caucus", "Biden", "Buttigieg", "Electability"]
word = word_list[random.randrange(0, (len(word_list) + 1))]
abcs = [chr(x) for x in range(65, 65+26)] # 65 is capital A on ASCII chart
incorrect_guesses = 0
done = False

print(gallows[0])
while not done:
    for letter in word:
        print("_")
    guess = input("Guess a letter: ").upper()
    if guess in word:
        print("Correct Guess!")

    if guess not in word:
        incorrect_guesses += 1
        print(gallows[incorrect_guesses])
    if incorrect_guesses > 8:
        print("You lost!")
        # replay = input(str(("Do you want to play again? Y or N: "))
        # if replay == Y.upper:
            # done = False
        # if replay == N.upper:
            # done = True