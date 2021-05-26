import random

comp_guess=random.randint(0,9)

print("Welcome to number Guesser Game")
print("You have to enter a number between 0 and 9 including both 0 and 9")
chanceleft=3
notwin=True
while notwin:
    user_guess=int(input("Write a number between 0 and 9 including 0 and 9"))


    if comp_guess>user_guess:
        print("Your guess is low")
    elif comp_guess<user_guess:
        print("Your guess is high")
    elif comp_guess==user_guess:
        print(f"Hurray You Cought the correct number. That is {comp_guess}")
        notwin=False
    if chanceleft==1:
        print(f"You are out of moves and the correct number is {comp_guess}")
        notwin=False

    chanceleft-=1

print("Bye")
#8 min