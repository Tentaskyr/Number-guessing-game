import random

def guess_game():
    random_number = random.randint(1, 100)
    print("Guess the number, between 1 and 100, and win a prize!")
    
    num_guesses = 0 
    while True:
        try:
            user_guess = int(input("What is your guess? "))
            num_guesses += 1 
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue 

        if user_guess < random_number:
            print("Your guess is low, try again!")
        elif user_guess > random_number:
            print("Your guess is high, try again!")
        else:
            print(f"You got it right! Great job! It took you {num_guesses} guesses.")
            break 

guess_game()
