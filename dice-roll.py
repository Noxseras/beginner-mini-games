import random

def numbers():
    diceNumber = [1, 2, 3, 4, 5, 6]
    throwDice = random.choice(diceNumber)
    print(f'The number you got is {throwDice}')
    return throwDice

def play():
    again = str(input('Throw?(if yes, type yes or y): '))
    while again == 'yes' or again == 'y':
        numbers()
        again = str(input('Throw?(if yes, type yes or y): '))
    else:
        print('Thank you for playing! Have a nice day! ')
        exit()
if __name__ == "__main__":
    play()