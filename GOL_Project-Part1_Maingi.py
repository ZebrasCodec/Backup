
# Samuel Maingi
# Assignment GOL 1
# 04/07/2023

 import pygame
# from random import randint
#
# # Set up Pygame
# pygame.init()
#
# # Set up the window
# MAX_ROW = 30
# MAX_COL = 60
# CELL_SIZE = 10
# WINDOW_WIDTH = MAX_COL * CELL_SIZE
# WINDOW_HEIGHT = MAX_ROW * CELL_SIZE
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#
# screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# import random
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
# def displayList(screen, lst):
#     cell_size = 10
#     for row in lst:
#         for col in range (len(lst[0])):
#             if lst[row][col] == 1:
#                 color = (green)
#             else:
#                 color = (black)
#         print(' '.join([str(col) for col in row]))
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
#         setZeroList(tempGen)
#         setInitialPatternList(tempGen)
#         copyList(tempGen, currentGen)
#         displayList(currentGen)
#     elif choice.upper() == 'Q':
#         print("\nThank you for playing my 1st version of Game of Life")
#         break


import random

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
    elif choice.upper() == 'Q':
        print("\nThank you for playing my 1st version of Game of Life")
        break