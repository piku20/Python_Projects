#Hangman

import random

words = ['terminator', 'avengers', 'titanic', 'iron man', 'Jungle Book']
word = random.choice(words).upper()
guesses = ''
lives = 9


print(word)
print('Guess the movie!')

while lives>0:
    not_guessed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=' ')
        elif char == ' ':
            print(' ', end=' ')
        else:
            print('_', end=' ')
            not_guessed += 1
    print()
            
    if not_guessed == 0:
        print('\nYou Win!')
        break
    
    guess = input('Enter an alphabet: ').upper()
    guesses += guess
    
    if guess not in word:
        lives -= 1
        print('Wrong')
        print(f'You only have {lives} lives left')

else:
    print('You Lose!')