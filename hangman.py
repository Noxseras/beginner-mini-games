import random
import string


# Function for the words
def wordList():
    words = ['Apple', 'Banana', 'Missisipi']
    randomWord = random.choice(words) # Choose a randmon word from the list 
    return randomWord.lower()

# Function for the hangman
def play():
    word = wordList() # Call the words fuction and assign it to word
    words_Letters = set(word) #letters in the word 
    alphabet = set(string.ascii_lowercase)
    wordsUsed = set() # what the user has used

    lives_left = 6 #attemps left for the user if types wrong character

    while len(words_Letters) > 0 and lives_left > 0: #while there are letters left in the word, repeat 
        print('The letters you have used so far:', ' '.join(wordsUsed))
        
        # what current word is guessed right 
        wordShown = [letter if letter in wordsUsed else '-' for letter in word]
        print('\nCurrent lives:',lives_left, 'and letters: ', ' '.join(wordShown))

        userLetter = input('Try guessing a letter: ') #Getting user's guess
        if userLetter in alphabet - wordsUsed : #Insures the user enters only letters from the alphabet
            wordsUsed.add(userLetter) #add the letter the user guessed in the guess words
            
            if userLetter in words_Letters: #if the user's input matches with the letter in the word, remove it from the word
                words_Letters.remove(userLetter)
            else:
                lives_left =lives_left - 1 #take 1 live if the the user types incorect letter 
                print('\nThat letter is not in the word!')
        
        elif userLetter in wordsUsed: #if the user has already guessed that letter, inform him
            print('\nYou have already entered that letter!')

        else: #in case the user does not enter anything from the alphabet
            print('\nInvalid input! Try again!')


    if lives_left == 0:
        print('\nGame Over! You do not have any lives left!')
    else:
        print(f'\nYou have found the word!! Good job! The word is \"{word}')
if __name__ == "__main__":
    play()