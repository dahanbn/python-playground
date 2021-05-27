import random

number = random.randint(0, 100)


def guessing_game():
    while s := input('Guess a number between 0-100: '):
        guess = int(s)
        if guess == number:
            print(f"You're right, the number was {s}")
            break
        elif guess > number:
            print(f"{s} is too high.")
        elif guess < number:
            print(f"{s} is too low.")


guessing_game()
