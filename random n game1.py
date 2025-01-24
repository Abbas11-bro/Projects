import random

lowest_num = 10
highest_num = 999
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select the number {lowest_num} between {highest_num}")

while is_running:

    guess = ("Enter your guess: ")
    
    if guess.isdigit():
        pass
    else:
        print("Invalid Guess")
        print(f"Please select the number {lowest_num} between {highest_num}")
