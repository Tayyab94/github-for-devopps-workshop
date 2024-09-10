"""this is game Rock - Paper """
import random
choices=("r","p","s")

while True:
    user_choice = input("Rock, Paper or scissors? (r/p/s) : ").lower()

    if user_choice not in choices:
        print("Invalid Choice!")
        continue
    computer_choice= random.choice(choices)
    print(f"YOu Choose :{user_choice}")
    print(f"Computer Choose: {computer_choice}")
    if user_choice ==computer_choice:
        print("Tie!")
    elif (
        (user_choice=="r" and computer_choice=="s") or 
        (user_choice=="s" and computer_choice=="p") or 
        (user_choice=="p" and computer_choice=="r")):
        print("you Win!")
    else:
        print("Computer Win!")

    should_continue= input("continue : (y/n): ").lower()
    if should_continue=='n':
        break
