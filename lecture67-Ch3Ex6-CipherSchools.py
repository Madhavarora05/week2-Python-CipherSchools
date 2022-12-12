#Number Guessing game
turns=0
import random
win=random.randint(1,100)
guess=False
while not guess:
    num=int(input("Guess the number?: "))
    if num<win:
        print("too low")
        turns+=1
    elif num>win:
        print("too high")
        turns+=1
    else:
        num==win
        turns+=1
        print(f"You won ,you guessed it in {turns}")
        guess=True