
# Samuel Maingi
# Assignment GOL 1
# 04/07/2023


import random
# import time
#
# MAX_ROW = 30
# MAX_COL = 60
#
# currentGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
# tempGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
#
# def displayMenu():
#     print("[P]lay – Press 'P' to play.")
#     print("[Q]uit – Press 'Q' to exit.")
#
# def displaySubMenu():
#     print("[S]top – Press 'S' to stop.")
#
# def setZeroList(lst):
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             lst[row][col] = 0
#
# def setInitialPatternList(lst):
#     row = random.randint(0, MAX_ROW - 6)
#     col = random.randint(0, MAX_COL - 7)
#     for i in range(6):
#         lst[row + i][col] = 1
#         lst[row + i][col + 6] = 1
#     for j in range(7):
#         lst[row + 5][col + j] = 1
#
# def copyList(src, dest):
#     for row in range(len(src)):
#         for col in range(len(src[0])):
#             dest[row][col] = src[row][col]
#
# def displayList(lst):
#     for row in lst:
#         print(' '.join([str(col) for col in row]))
#
# def getNeighbors(lst, row, col):
#     count = 0
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             r = (row + i + MAX_ROW) % MAX_ROW
#             c = (col + j + MAX_COL) % MAX_COL
#             count += lst[r][c]
#     count -= lst[row][col]
#     return count
#
# def setNextGenList():
#     global currentGen, tempGen
#     setZeroList(tempGen)
#     for row in range(MAX_ROW):
#         for col in range(MAX_COL):
#             n = getNeighbors(currentGen, row, col)
#             if currentGen[row][col] == 1 and n < 2:
#                 tempGen[row][col] = 0
#             elif currentGen[row][col] == 1 and (n == 2 or n == 3):
#                 tempGen[row][col] = 1
#             elif currentGen[row][col] == 1 and n > 3:
#                 tempGen[row][col] = 0
#             elif currentGen[row][col] == 0 and n == 3:
#                 tempGen[row][col] = 1
#     copyList(tempGen, currentGen)
#
# displayMenu()
# setZeroList(tempGen)
# setInitialPatternList(tempGen)
# copyList(tempGen, currentGen)
# displayList(currentGen)
#
# while True:
#     choice = input("Enter your choice: ")
#     if choice.upper() == 'P':
#         while True:
#             displaySubMenu()
#             setNextGenList()
#             displayList(currentGen)
#             time.sleep(0.1)
#             if input("Press any key to continue, or 'S' to stop: ").upper() == 'S':
#                 setZeroList(tempGen)
#                 setInitialPatternList(tempGen)
#                 copyList(tempGen, currentGen)
#                 displayList(currentGen)
#                 break
#     elif choice.upper() == 'Q':
#         print("\nThank you for playing my 1st version of Game of Life")
#         break


import random
import os
import time

MAX_ROW = 30
MAX_COL = 60

currentGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
tempGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]

def displayMenu():
    print("[P]lay – Press 'P' to play.")
    print("[Q]uit – Press 'Q' to exit.")

def setZeroList(lst):
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            lst[row][col] = 0

def setInitialPatternList(lst):
    row = random.randint(0, MAX_ROW - 6)
    col = random.randint(0, MAX_COL - 7)
    for i in range(6):
        lst[row + i][col] = 1
        lst[row + i][col + 6] = 1
    for j in range(7):
        lst[row + 5][col + j] = 1

def copyList(src, dest):
    for row in range(len(src)):
        for col in range(len(src[0])):
            dest[row][col] = src[row][col]

def displayList(lst):
    for row in lst:
        print(' '.join([str(col) for col in row]))

def displaySubMenu():
    print("[S]top – Press 'S' to stop.")

def setNextGenList():
    global currentGen
    global tempGen
    for row in range(1, MAX_ROW - 1):
        for col in range(1, MAX_COL - 1):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbors += currentGen[row + i][col + j]
            neighbors -= currentGen[row][col]
            if currentGen[row][col] == 1 and (neighbors < 2 or neighbors > 3):
                tempGen[row][col] = 0
            elif currentGen[row][col] == 0 and neighbors == 3:
                tempGen[row][col] = 1
            else:
                tempGen[row][col] = currentGen[row][col]

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

displayMenu()
setZeroList(tempGen)
setInitialPatternList(tempGen)
copyList(tempGen, currentGen)
displayList(currentGen)

while True:
    choice = input("Enter your choice: ")
    if choice.upper() == 'P':
        setZeroList(tempGen)
        setInitialPatternList(tempGen)
        copyList(tempGen, currentGen)
        displayList(currentGen)
        while True:
            displaySubMenu()
            setNextGenList()
            clearScreen()
            displayList(currentGen)
            copyList(tempGen, currentGen)
            time.sleep(0.2)
            if input().upper() == 'S':
                break
    elif choice.upper() == 'Q':
        print("\nThank you for playing my 2nd version of Game of Life")
        break


