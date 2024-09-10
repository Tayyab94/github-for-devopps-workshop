"""This is Guess name we have created for the login building.."""

import random

number_to_guess= random.randint(1,100)
while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))

      if guess < number_to_guess:
         print("Too LOW!")
      elif guess > number_to_guess:
        print("Too High!")
      else:
       print("You guessed it! Congrats")
       break
    except ValueError:
        print("Invalid input. Please enter a number.")

