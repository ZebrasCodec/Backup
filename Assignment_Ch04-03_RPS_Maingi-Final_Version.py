# Samuel Maingi
# Assignment 05-2
# 03/14/2023

import random

rk = ["Rock", "rock", "r", "R"]
pp = ["Paper", "paper", "p", "P"]
sc = ["Scissors", "scissors", "s", "S"]

def collectStringInput():
    rps = ["R", "r", "rock", "Rock", "P", "Paper", "p", "paper", "S", "Scissors", "scissors", "s"]
#    rps = [rk,pp,sc]
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
    if (user in rk and comp in rk) or \
       (user in pp and comp in pp) or \
       (user in sc and comp in sc):
        return "Tie"
    elif (user in f"{rk}" and comp in f"{sc}") or \
         (user in f"{pp}" and comp in f"{rk}") or \
         (user in f"{sc}" and comp in f"{pp}"):
        return "Player"
    else:
        return "Computer"


def reasoning(user,comp):
    if (user in rk or comp in rk) and (comp in sc or user in sc):
        return "Rock crushes Scissors"
    elif (user in pp or comp in pp) and (comp in rk or user in rk):
        return "Paper beats Rock (somehow)"
    elif (user in sc or comp in sc) and (comp in pp or user in pp):
        return "Scissors cut Paper"





print("Hi there! Wanna play Rock, Paper Scissors?")
user = collectStringInput()
comp = convertIntegerToRPS()
why = reasoning(user,comp)
print(f"Player: {user}\n"
      "\n"
      f"Computer's selection: {comp}")

winner = evaluateWinning(user, comp)
if winner == "Tie":
    print("It's a Tie!")
else:
    print(f"{why}\n"
          f"The {winner} wins!")