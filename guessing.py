#!/bin/python3
import random

while True:
    random_number = random.randint(1,10)

    try:
        user_number = int(input("Please pick a number between 1 and 10: "))
    except ValueError:
        print("Please enter an Integer only.")
        continue

    if user_number < random_number:
        print(f"Too Low (computer picked: {random_number}).")
    elif user_number > random_number:
        print(f"Too high (computer picked: {random_number}).")
    else:
        print("You got it!")
    
    answer = input("Do you want to play again? <y/n> ").lower()
    if not answer in ['y','yes']:
        print("Bye!")
        break
