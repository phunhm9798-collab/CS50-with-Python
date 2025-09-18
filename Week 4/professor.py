# Import the necessary module
import random

# Define a function that acts as the structure of the game, and carries out operations based on it


def main():
    level = get_level()
    error = 0
    score = 0
    for _ in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = str(x+y)
        res = 0

        for i in range(4):
            if i == 3:
                print(x, '+', y, '=', answer)
                break

            print(x, '+', y, '=', end=' ')
            res = input()
            if res != answer:
                print('EEE')
            else:
                score += 1
                break

# Define a function that gets the user's input for a level, then compare to see if it is suitable


def get_level():
    while True:
        try:
            l = int(input('Level: '))
        except ValueError:
            pass
        else:
            if l == 1 or l == 2 or l == 3:
                return l
            else:
                pass


# Define a function that generates a random integer based on the user's inputted level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
