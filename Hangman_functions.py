#---------------------------------------#
#Functions for my Hangman game          #
#Creator: Tobias Weber aka MisterNSA    #
#Date: 09.04.2020                       #
#---------------------------------------#
import random



#Takes a File and moves all word into a list
def Word_import():

    word_list = []

    word_source = open('Wörter.txt', 'r')

    for word in word_source: 

        word_list.append(word)  

    word_source.close()
    return(word_list)




#returns a random word from the list
def Random_word(word_list):  

    word = random.choice(word_list)
    word = word.lower() 
    word = word.strip() #remove \n 
    return(word)



#Show the current Informations of the Game
def displayBoard(correctLetters, current_word, wrongLetters):

    HANGMANPICS = Hangmanpics()
    print(HANGMANPICS[len(wrongLetters)]) #current picture of Hangma
    print()

    if len(wrongLetters) > 0:
        print("Wrong letters:", end=" ") 

    for letter in wrongLetters:

        print(letter, end=", ") 

    print()
    blanks = "_" * len(current_word) 
        
    for i in range(len(current_word)): # replace blanks with correctly guessed letters
        
        if current_word[i] in correctLetters:

            blanks = blanks[:i] + current_word[i] + blanks[i+1:]
        
    for letter in blanks: # show the secret word with spaces in between each letter

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

        elif guess not in "abcdefghijklmnopqrstuvwxyz": #Wenn kein Buchstabe

            print("Please enter a LETTER.")

        else:

            return guess



# This function returns True if the player wants to play again (y), otherwise it returns False.
def playAgain():

    return input("Do you want to play again? (yes or no) ").lower().startswith("y") 



#returns the List of Pictures - Didnt wanted it to be in the main
def Hangmanpics():
#list of pictures | 9
    HANGMANPICS = ['''

    =========''','''

      +---+
          |
          |
          |  
          |
          |
    =========''','''

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
    return HANGMANPICS
    