# Import the necessary modules
import random as rd
from sys import exit

# Define a loop that gets the user's input (level)
while True:
    try:
        n = int(input('Level:'))
    except ValueError:
        continue
    else:
        if n < 0 or n == 0:
            pass
        else:
            break

# Randomly generate a number for comparision
x = rd.randint(1, n)

# Define a loop that get the user's guess
while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        pass
    else:
        if guess > x:
            print('Too large!')
        elif guess < x:
            print('Too small!')
        else:
            print('Just right!')
