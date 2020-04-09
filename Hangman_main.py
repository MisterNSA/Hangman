#---------------------------------------#
#My Version of the popular Hangman game #
#Creator: Tobias Weber aka MisterNSA    #
#Date: 09.04.2020                       #
#---------------------------------------#
import Hangman_functions as Hf


def HangMAIN(): #ba dum tss

    


    print("H A N G M A N")
    #missedLetters = ""
    wrongLetters = ""
    correctLetters = ""
    word_list = Hf.Word_import() #import the words
    current_word = Hf.Random_word(word_list) #choose a random word

    gameIsDone = False

    while True:

        Hf.displayBoard(correctLetters, current_word, wrongLetters)
        HANGMANPICS = Hf.Hangmanpics()

        # Let the player type in a letter.
        guess = Hf.getGuess(wrongLetters + correctLetters)

        if guess in current_word:

            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True

            for i in range(len(current_word)):

                if current_word[i] not in correctLetters: #checks if all letters from word are guessed
                    foundAllLetters = False
                    break

            if foundAllLetters:

                print("Yes! The word is " + current_word + "! You have won!")
                gameIsDone = True

        else:

            wrongLetters = wrongLetters + guess

            # Check if player has guessed too many times and lost
            if len(wrongLetters) == len(HANGMANPICS) - 1:

                Hf.displayBoard(HANGMANPICS, wrongLetters, correctLetters, current_word)
                print("You have run out of guesses!\n")
                print("After " + str(len(wrongLetters)) + " wrong guesses and " + str(len(correctLetters)) + " correct guesses, the word was " + current_word)
                gameIsDone = True

            # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if Hf.playAgain():
                HangMAIN()
            else:
                break

if __name__ == "__main__":
    HangMAIN()