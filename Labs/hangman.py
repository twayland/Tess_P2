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
word_list = ["IOWA", "SANDERS", "CAUCUS", "BIDEN", "WARREN", "PRIMARY"]  # options for hangman
abcs = [chr(x) for x in range(65, 65+26)]  # 65 is capital A on ASCII chart  # alphabet
incorrect_guesses = []
correct_guesses = []
my_word = word_list.pop(random.randrange(len(word_list)))  # pick random word
blanks = len(my_word)  # to keep track of win
done = False  # for loop

print("Welcome to Iowa Caucus Hangman!")

while not done:
    print("Wrong guesses: ", incorrect_guesses)  # so user knows wrong guesses
    print(gallows[len(incorrect_guesses)])  # print gallows depending on incorrect answers
    correct = True
    for letter in my_word:  # print blanks or letter depending on guess
        if letter in correct_guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    user_guess = input("Guess a letter: ").upper()  # user input

    if user_guess in abcs:  # check in alphabet
        if user_guess in correct_guesses or user_guess in incorrect_guesses:  # check that they haven't guessed
            print("You already guessed this.")
        if user_guess not in my_word: # check if it's in word
            print("Incorrect guess.")
            incorrect_guesses.append(user_guess)
        elif user_guess in my_word:  # if is in word, make used, give feedback
            correct_guesses.append(user_guess)
            print("Correct Guess!")
            blanks -= my_word.count(user_guess)  # to track win
    else:
        print("Not a letter. Try again!")

    if blanks <= 0:
        print("The word was " + my_word + ".")
        print("You guessed the word. Congrats, winner.")
        done = True
    if len(incorrect_guesses) == 6:
        print("The word was" + my_word + ".")
        print("You lost!")
        done = True
