# Random NUmber guess game:

import random



print('Press 1 - AI asks , Player guesses.\nPress 2 - Player asks, AI guesses.\nPress 3 - Watch AI ask and guess.\n')

choice = int(input(f'Enter a number: '))

def func1():
    #print('This is f1')
    random_number = random.randint(1,10)
    guess = 0

    print(random_number)

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and 10: '))
    
        if guess<random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
        
    else:
        print (f'Congrats! you have guess the number {random_number}')
    
def func2():
    #print('This is f2')
    print("Guess a number from 1 to 100\n\n")

    low = 1
    high = 100
    feedback =''
    
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high(h), too low(l) or correct(c): ')
        
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
            
    else:
        print(f'\nComputer guessed your number: {guess}')
    
def func3():
    #print('This is f3')
    low = 1
    high = 100
    feedback = ''
    
    random_number = random.randint(low, high)
    print (random_number)
    
    while feedback != 'correct':
        guess = random.randint(low, high)
        print(f'Is it {guess}?: ', end='')
        
        
        if guess > random_number:
            feedback = 'high'
            print(f'That\'s {feedback}')
            high = guess - 1
            
        elif guess < random_number:
            feedback = 'low'
            print(f'That\'s {feedback}')
            low = guess +1
            
        else:
            feedback = 'correct'
            print('Yes!')
                
    else:
        
        print(f'\nThe correct guess is {guess}')


if choice == 1:
    func1()
elif choice ==2:
    func2()
elif choice ==3:
    func3()
else:
    print('Sorry, invalid input!')