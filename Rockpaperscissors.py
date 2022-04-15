import random

print("*********Rock Paper Scissors**********")
name = input("Enter your name:")

print("Welcome",name)

print("Rules:\
    0 for Rock\
    1 for Paper\
    2 for scissors")

computer_guess = random.randint(0,2)

chance = True
while chance:
    
    user_guess = int(input("What is guess!"))
    if user_guess > 2:
        print("Please enter the number between 0-2")
    elif user_guess == computer_guess:
        print("Match tie")
    elif user_guess == 0:
        if computer_guess == 1:
            print("computer is won (Paper)")
        else:
            print(f"{name} winner")
    elif user_guess == 1:
        if computer_guess == 2:
            print("computer is won (Scissors)")
        else:
            print(f"{name} winner")
    elif user_guess == 2:
        if computer_guess == 0:
            print("computer is won (Rock)")
        else:
            print(f"{name} winner")
    chance = False 

