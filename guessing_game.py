"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

Created by: Paul Liao

"""

import random


# Create highscore list to hold of the high scores
highscore = []

# Display high score
def print_highscore():
    if len(highscore) == 0:
        print("The current HIGHSCORE is 0\n")
    else:
        highscore.sort()
        int_hs = highscore[0]        
        print("\nThe current HIGHSCORE is {}\n".format(int_hs))


# Start game function
def start_game():
    
    # Generate and store a random number called answer
    answer = random.randint(1,10)
    
    # Create a variable for number of tries
    attempt = 0
            
    # Prompt user for a number between 1 - 10
    while True:
        guess = input("Pick a number between 1 - 10: ")
        
        try:
            guess = int(guess)            
            
            if guess > 10 or guess < 1:
                raise Exception("Invalid range. Please only pick a number between 1 - 10.")             
        
            if guess < answer:
                print("It is higher!")
            elif guess > answer:
                print("It is lower!")
            elif guess == answer:
                print("You've got it!")
                attempt += 1
                print("You have made {} attempt/s.".format(attempt))
                highscore.append(attempt)
                highscore.sort()
                break
            
        except ValueError:
            print("We ran into an issue. Please try again.")
            attempt -= 1
        except Exception as err:
            if err:
                print("{}".format(err))
            attempt -= 1
                        
        attempt += 1


# Retry function would retrun 1 or 0 for correct answer. It will loop if user fails to enter the correct response
def retry_game():
    while True:
        retry = input("Would you like to start again? [Y/N] ")
        retry = retry.lower()    
        if retry == 'y':
            return 1
            break
        elif retry == 'n':
            return  0 
            break
        else:
            print("Please enter Y or N")
            continue
    
# Display welcome message 
print("""
      ----------------------------------------
        Welcome to the Number Guessing Game!
      ----------------------------------------                   
      """)

# Ask the player if you want to play the game again
while True:    
    print_highscore()
    start_game()    
    
    retry = retry_game()
    
    if retry == 1:
        continue    
    elif retry == 0:
        print("Thank you for playing!")
        break