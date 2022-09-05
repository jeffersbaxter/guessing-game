import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. 'easy' or 'hard': ")

guesses_remaining = 10

if difficulty == 'hard':
    guesses_remaining = 5

number = random.randint(1, 100)
guess = 0
while guesses_remaining > 0 and guess != number:
    print(f"You have {guesses_remaining} guesses remaining.")
    guess = int(input("Make a guess: "))
    if guess > number:
        guesses_remaining -= 1
        print("Too high. Guess again!")
    elif guess < number:
        guesses_remaining -= 1
        print("Too low. Guess again!")

if guesses_remaining == 0 and guess != number:
    print(f"You lose! The correct number was {number}")
else:
    print(f"You win! The correct number was {number}")