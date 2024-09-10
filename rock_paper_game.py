"""This is the Rock - Paper - Scissors game."""

import random

choices = ("r", "p", "s")

# Winning combinations dictionary
winning_combinations = {
    "r": "s",  # Rock beats Scissors
    "s": "p",  # Scissors beat Paper
    "p": "r",  # Paper beats Rock
}

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie!")
    elif winning_combinations[user_choice] == computer_choice:
        print("You Win!")
    else:
        print("Computer Wins!")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        break
