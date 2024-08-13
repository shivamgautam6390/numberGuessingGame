# Number guessing game using python
#import a random module
import random

#creating a function which generate a random number and guess the user input
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    #set the range for the secret number
    lower_limit=1
    upper_limit=100
    secret_number=random.randint(lower_limit,upper_limit)

    attempts=0

    while True:
        # get user input
        guess=int(input(f"Guess the number between {lower_limit} and {upper_limit}"))

        # increment the attempts count
        attempts+=1

        # check the guess
        if guess == secret_number:
            print(f"congratulations! you guessed the coreect number in {attempts} attempts. your number is : {secret_number}")
            break
        elif guess<secret_number:
            print("Too low . Try again.")
        else:
            print("Too high . Try again.")


if __name__ == "__main__":
    number_guessing_game()


