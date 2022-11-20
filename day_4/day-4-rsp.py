import random

user_rsc = int(input("What do you choose? Type 0 for Rock, 1 for Scissors or 2 for Paper"))
com_rcs = random.randint(0, 2)

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

rcss = [rock, scissors, paper]

print(f"rcss[com_rcs]={rcss[com_rcs]}")


if com_rcs == 0 and user_rsc > 0:
    print("You Win")
elif com_rcs == user_rsc:
    print("Draw")


