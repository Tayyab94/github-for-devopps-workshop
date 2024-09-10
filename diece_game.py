"""
    this is dice role Game which we have created just for demo 
"""

import random

while True:
    choice= input("Roll the dice (y/n) : ").lower()
    if choice =='y':
        diece= random.randint(1,6)
        diece1= random.randint(1,6)
        print(f"({diece},{diece1})")
    elif choice =='n':
        break
    else:
        print("Invalid Choice")
