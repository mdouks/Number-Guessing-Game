"""
Project 1 - Number Guessing Game
--------------------------------
"""
import random
import statistics

def start_game():
    
    print("Welcome to **Guess** **That** **Number**")
    print("Instructions: Guess a number between 1 and 100!")

    count = 0
    attempts = []
    solution = random.randint(1, 100)

    while True:

        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
            if type(guess) != int:
                raise TypeError
            if guess < 0 or guess > 100: 
                raise ValueError(f'{guess} not within range. Enter a number *BETWEEN 1-100')
        except (ValueError, TypeError) as err:
            print(f'{err}. Enter a *NUMBER BETWEEN 1-100*. Please try again')
        else:
            if guess > solution:
                print("It's lower.")
                count += 1
                continue
            elif guess < solution:
                print("It's higher.")
                count += 1
                continue
            else:
                print("Got it")
                count += 1
                attempts.append(count)
                print(f'****It took you {count} tries to guess {solution} correctly')
                print(f'****mean attempts to solve: {statistics.mean(attempts)}')
                print(f'****mode attempts to solve: {statistics.mode(attempts)}')
                print(f'****median attempts to solve: {statistics.median(attempts)}')
                again = input("Do you want to play again? (Y/N) ")
                print(f'****HIGH SCORE: {min(attempts)}')
                if again.upper() == 'N':
                    break
                else:
                    solution = random.randint(1, 100)
                    continue

    print('Game is over. GOOBYE!')



start_game()