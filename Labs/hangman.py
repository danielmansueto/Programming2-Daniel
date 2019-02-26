'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game
import random

picture = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print()
word_list = ["pizza", "spaghetti", "cookies", "chicken", "burrito", "pasta", "salad", "omelet", "quiche", "crepe",
             "artichoke", "macaroni", "avocado", "cinnamon", "empanada", "vanilla"]
wrong_list = []


def hangman():
    correct_guesses = 0
    incorrect_guesses = 0
    play_again = ""
    done = False
    my_word = word_list.pop(random.randrange(len(word_list)))
    print("Welcome to Hangman!")

    while done is False:
        print(picture[incorrect_guesses])

        print("Used Letters: ", end=" ")
        for i in range(len(wrong_list)):
            wrong = wrong_list[i]
            print(wrong, end=" ")

        print()

        for picked_letter in my_word:
            if picked_letter in wrong_list:
                print(picked_letter, end=" ")
            else:
                print("_", end=" ")
        print()

        print()
        picked_letter = input("Pick a Letter: ")
        picked_letter.lower()
        if picked_letter in wrong_list:
            print("Already Used")
        else:
            wrong_list.append(picked_letter)
        if picked_letter in my_word:
            correct_guesses += 1
        else:
            incorrect_guesses += 1

        print()

        if correct_guesses == len(my_word):
            print("You Won!")
            play_again = input("Would You like to play again?")
        if incorrect_guesses >= 6:
            print(picture[incorrect_guesses])
            print("You Lost :(")
            print("Your word was ", my_word)
            play_again = input("Would You like to play again?")
        if play_again.lower() == "yes" or play_again.lower() == "yes":
            hangman()
        if play_again.lower() == "no" or play_again.lower() == "no":
            print("Thank you for playing")
            done = True

hangman()
