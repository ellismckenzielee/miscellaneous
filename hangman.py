import requests
import random

play = input('Do you want to play Hangman?: \n 1. yes \n 2. no ')

#Functions
def printInformation(count, chosen_letters):
    '''Displays the number of attempts remaining and letters preiously chosen'''
    print('Attempts left: ' + str(9 - i))
    print('You have previously chosen: ' + chosen_letters)

def chooseLetter(chosen_letters):
    '''Prompts user for input and checks if letter has already been entered'''
    chosen_letter = 'placeholder'
    while chosen_letter not in chosen_letters:
        chosen_letter = input('Please select a letter: ').lower()
        if (chosen_letter not in chosen_letters) and (chosen_letter in 'abcdefghijklmnopqrstuvwxyz'):
            chosen_letters += chosen_letter  
        else: 
            chosen_letter = 'placeholder'
            print('Pick a letter from a-z, that has not been picked before')
    return chosen_letters, chosen_letter

def WORD_splitUpdater(WORD_split, WORD, chosen_letter):
    '''Updates the WORD_split variable, which tells the user which characters selected are in the word'''
    in_word = False
    complete = False
    for index, char in enumerate(WORD):
        if char == chosen_letter:
            WORD_split[index] = chosen_letter   
            in_word = True
    print('WORD: ' + ''.join(WORD_split))
    if '-' not in WORD_split:
        complete = True
    return WORD_split, in_word, complete


#Main Loop
while play == 'yes':
    #Get word and initialize variables
    word_site = word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    selector = random.randint(0, len(WORDS))
    WORD = WORDS[selector].decode("utf-8")
    WORD = WORD.lower()
    WORD_split = list('-'*len(WORD))
    chosen_letters = ''
    i = 0
    print('WORD: ' + ''.join(WORD_split))
    
    while i <= 9:
        if i == 9:
            print('Unforuntately you failed! The word was:', WORD)
            play = input('Play again?: \n 1. yes \n 2. no ')
            break
        chosen_letter = ''
        printInformation(i, chosen_letters)
        chosen_letters, chosen_letter = chooseLetter(chosen_letters)
        WORD_split, in_word, complete = WORD_splitUpdater(WORD_split, WORD, chosen_letter)
        
        if complete == True:
            i = 12
            print('Well done, the word was: ' + WORD)
            play = input('Play again?: \n 1. yes \n 2. no ')

        if in_word == False:
            i += 1
        
        