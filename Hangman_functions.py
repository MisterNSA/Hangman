#---------------------------------------#
#Functions for my Hangman game          #
#Creator: Tobias Weber aka MisterNSA    #
#Date: 09.04.2020                       #
#---------------------------------------#
import random


# Exports words from a file into a list
def Word_import():

    word_list = []
    word_source = open('Wörter.txt', 'r')

    for word in word_source:
        word_list.append(word)
    word_source.close()
    return(word_list)


# Returns a random word from the list
def Random_word(word_list):

    word = random.choice(word_list)
    word = word.lower()
    word = word.strip()  # remove \n
    return(word)


# Shows the current Informations of the Game
def displayBoard(correctLetters, current_word, wrongLetters):

    # Select current Picture for amount of wrong letters
    HANGMANPICS = Hangmanpics()
    print(HANGMANPICS[len(wrongLetters)])

    # Print wrong letters if there are any
    if len(wrongLetters) > 0:
        print("Wrong letters: ")
        for wletter in wrongLetters:
            print(wletter, end=", ")
        print()

    # Shows how much letters the word has and replaces blanks with correctly guessed letters
    blanks = "_" * len(current_word)
    for letter in range(len(current_word)):
        if current_word[letter] in correctLetters:
            blanks = blanks[:letter] + current_word[letter] + blanks[letter+1:]

    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=" ")
    print()


# Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
def getGuess(alreadyGuessed):

    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":  # Wenn kein Buchstabe
            print("Please enter a LETTER.")
        else:
            return guess


# This function returns True if the player wants to play again (y), otherwise it returns False.
def playAgain():

    return input("Do you want to play again? (yes or no) ").lower().startswith("y")


# returns the List of Pictures - Didnt wanted it to be in the main
def Hangmanpics():
    # list of all 9 pictures #Writen in all Uppercase cause its a constant
    HANGMANPICS = [
        '''

    =========
    ''', '''

      +---+
          |
          |
          |  
          |
          |
    =========
    ''', '''

      +---+
      |   |
          |
          |
          |
          |
    =========
    ''', '''

      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''']
    return HANGMANPICS
