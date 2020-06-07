import random

import cprint
import termcolor

word_chosen = ''
hangman_status = ''
status = -1
underscores = ''
words_guessed = []
guess = ''
lives = 6

with open('hangman_status.txt','r') as statusfile:
    hangman_status = statusfile.read()
    hangman_status = hangman_status.split('@')


with open('words_for_hangman.txt','r') as wordsfile:
    word_chosen = wordsfile.read()
    word_chosen = word_chosen.split('\n')

word_chosen = random.choice(word_chosen)
underscores = '_' * len(word_chosen)
underscores = list(underscores)

while lives > 0:
    print("\nTake A Guess!")
    print(''.join(underscores))
    guess = input("")

    if guess == word_chosen:
        termcolor.cprint("Congratulations, You Guessed The Word!","green")
        break

    elif guess in words_guessed:
        termcolor.cprint("You already guessed that!","yellow")
    
    elif guess in word_chosen and guess != '':
        termcolor.cprint("Good Guess!", "green")
        for letter in word_chosen:
            if guess == letter:
                underscores[word_chosen.index(letter)] = letter
    
    else:
        termcolor.cprint("Oops! Wrong Guess, try again!","red")
        lives -=1
        status += 1
        print(hangman_status[status])
    words_guessed.append(guess)

if lives == 0:
    termcolor.cprint(f"Oops, you failed, the word was {word_chosen}", "red")

