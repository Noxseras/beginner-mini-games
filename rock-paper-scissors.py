import random


# 1)s > p,    2)p > r,    3) r > s
def play():
    user_input = input("Type 'r' for rock, 'p' for paper ,and 's' for scissors: " ) # ask the user to type his choise
    computer_choise = random.choice(['r', 'p', 's']) # randomly select for the computer 
    if (user_input == 's' and computer_choise == 'p') or (user_input == 'p' and computer_choise == 'r') or (user_input == 'r' and computer_choise == 's'):
        print('\nYou won!')

    elif user_input == computer_choise:
        print("\nIt's a tie!!")

    elif not user_input == ('r' or 'p' or 's'):
        print('\nInvalid input!')

    else:
        print ('\nYou lost!')

if __name__ == "__main__":
    play()