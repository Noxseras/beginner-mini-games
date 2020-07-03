import random

def numbers(): # Fuction for a number to be randomly guessed
    number_list = [] # empty list for the range of the numbers
    for number in range(1,20): 
        number_list.append(number) #add append the number in a list 
    random_number = random.choice(number_list) # randomly choose a number
    return random_number

def player():
    random_number = numbers() # call numbers
    user_input = input('Try guessing a number, from 1 to 20: ')
    # check if the user's input is the same as the computer's choise
    if (user_input == random_number):
        print(f'Yayy, you guessed the number correctly!! The number was: {random_number}' )
    else:
        print(f'You did not guessed the number! The number was: {random_number}')

if __name__ == "__main__":
    numbers()
    player()