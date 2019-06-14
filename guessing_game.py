"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

Created by: Paul Liao

"""

import random


# Display high score
def print_highscore():
    if len(highscore) == 0:
        print("The current high score is 0")
    else:
        highscore.sort()
        int_hs = highscore[0]        
        print("The current high score is {}".format(int_hs))


# Start game function
def start_game():
   
    # Generate and store a random number called answer
    answer = random.randint(1,10)
    
    # Create a variable for number of tries
    attempt = 0

    # Display welcome message 
    print("""
          ----------------------------------------
            Welcome to the Number Guessing Game!
          ----------------------------------------                   
          """)

    print_highscore()
            
    # Prompt user for a number between 1 - 10
    while True:
        guess = input("Pick a number between 1 - 10: ")
        guess = int(guess)
        if guess < answer:
            print("It is higher!")
            attempt += 1
            print("{}".format(attempt))
        elif guess > answer:
            print("It is lower!")
            attempt += 1
            print("{}".format(attempt))
        elif guess == answer:
            print("You've got it!")
            attempt += 1
            print("You have made {} attempt/s.".format(attempt))
            highscore.append(attempt)
            highscore.sort()
            break
        

# Create highscore list to hold of the high scores
highscore = []

# Ask the player if you want to play the game again
while True:
    start_game()
    
    retry = input("Would you like to start again? [Y/N] ")
    retry = retry.lower()
    
    if retry == 'n':
        print("Thank you for playing!")
        break
