import random


def computer_guess(num):
    # start and stop value for random number in between this numbers
    start = 1
    stop = num
    feedback = ''  # Empty string for checking user input
    # this if else block of code give trys for player given number based
    if num < 100:
        trys = 5
    elif 100 <= num <= 1000:
        trys = 10
    else:
        trys = 15

    while feedback != 'c' or trys != 0:
        print()
        print(f"YOU have {trys} balance")
        # reduce trys one by one
        trys = trys - 1
        print(f"try to guess in between {start} to {stop}")

        if start != stop:
            guess = random.randint(start, stop)
            print(f"computer guess is {guess}")
        else:
            guess = stop
        feedback = input("(c)stands for correct,(l) stands for  low,(h) stands for high :").lower()
        if feedback == 'l':
            stop = guess - 1
        elif feedback == 'h':
            start = guess + 1
        elif feedback == 'c':
            trys = 0


def user_guess(num):
    start = 1
    stop = num
    run = ''
    chance = 5
    com_guess = random.randint(start, stop)
    print(com_guess)
    while run != 't' and chance != 0:
        print(" ")
        print(f"You have {chance} chance")
        chance = chance - 1
        guess = int(input(f"In between {start} to {stop} : "))

        if com_guess == guess:
            print("YOu win,computer guess is  {}".format(com_guess))
            run = 't'

        elif com_guess < guess:
            print("low number ")

        elif com_guess > guess:
            print("high number")


user_guess(10)
