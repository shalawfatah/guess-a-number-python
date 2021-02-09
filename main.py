import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        count += 1
        guess = int(input(f'Guess a number between 1 and {x}, RULE: You only SIX attempts, make the most of it: '))
        if guess < random_number:
            print('Sorry, too low, guess again! ')
        elif guess > random_number:
            print('Sorry, too high, guess again! ')
        if count >= 6:
            print(f'::::::::::::::::: GAME OVER! SORRY, GOOD LUCK NEXT TIME ::::::::::::::::: THE CORRECT GUESS IS: {random_number}')
            break;
        elif guess == random_number:
            print(f'::::::::::::::::: Yay, you guessed the number correctly ::::::::::::::::: It is: {random_number}!')
guess(100)