# Samuel Maingi
# Assignment 04-3
# 02/13/2023

import random


def collectStringInput():
    rps = ["R", "r", "rock", "P", "p", "paper", "S", "scissors", "s"]
    while True:
        user = input("Enter [R]ock, [P]aper, or [S]cissors: ")
        if user in rps:
            return user
        else:
            print("Invalid choice. Please try again.")


def generateIntegerValue():
    return random.randint(1, 90)


def convertIntegerToRPS():
    num = generateIntegerValue()
    if num <= 30:
        return "Rock"
    elif num <= 60:
        return "Paper"
    else:
        return "Scissors"


def evaluateWinning(user, comp):
    if user == comp:
        return "Tie"
    elif (user in f"{rk}" and comp in f"{sc}") or \
         (user in f"{pp}" and comp in f"{rk}") or \
         (user in f"{sc}" and comp in f"{pp}"):
        return "User"
    else:
        return "Computer"


def reasoning():
    if user in rk and comp in sc:
        return "Rock crushes Scissors"
    elif user in pp and comp in rk:
        return "Paper beats Rock (somehow)"
    elif user in sc and comp in pp:
        return "Scissors cut Paper"


rk = ["Rock", "rock", "r", "R"]
pp = ["Paper", "paper", "p", "P"]
sc = ["Scissors", "scissors", "s", "S"]


print("Hi there! Wanna play Rock, Paper Scissors?")
user = collectStringInput()
comp = convertIntegerToRPS()
res = reasoning()
print(f"Player: {user}\n"
      "\n"
      f"Computer's selection: {comp}")
winner = evaluateWinning(user, comp)
if winner == "Tie":
    print("It's a Tie!")
else:
    print(f"{res}\n"
          f"The {winner} wins!")