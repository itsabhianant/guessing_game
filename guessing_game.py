import random

def computer_guess(x):
    """Makes computer guess the right number a user thinks of."""

    low = 1 
    high = x
    response = ""

    while response != 'c':

        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low 
            print(f"I guessed your number and it is...{guess}")
            break

        response = input(f"Is {guess} the number you guessed? Is it high(h), low(l) or correct(c)? ").lower()

        if response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        elif response == 'c':
            print(f"Look, I correctly guessed your number as {guess}")
        else:
            print("You don't deserve to play this game. You are a retarded human who can't even follow rules.")
            break

    
computer_guess(100)

# You can change the range of the game by replacing 10 in computer_guess(10)
#For ex: if you want to the computer to guess b/w 1 to 100 just change computer_guess(10) to computer_guess(100)