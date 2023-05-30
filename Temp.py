
# Samuel Maingi
# Assignment GOL 1
# 04/07/2023

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
# def displayList(lst):
#     for row in lst:
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
#         break




# import pygame
# import random
#
# MAX_ROW = 30
# MAX_COL = 60
#
# currentGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
# tempGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
#
# def displayMenu(screen):
#     font = pygame.font.Font(None, 30)
#     text = font.render("Press 'P' to play or 'Q' to quit.", True, (255, 255, 255))
#     screen.blit(text, (10, 10))
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
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             color = (0, 0, 0) if lst[row][col] == 0 else (0, 255, 0)
#             pygame.draw.rect(screen, color, (col*cell_size, row*cell_size, cell_size, cell_size))
#
# pygame.init()
#
# # Set up the window
# CELL_SIZE = 10
# WINDOW_WIDTH = MAX_COL * CELL_SIZE
# WINDOW_HEIGHT = MAX_ROW * CELL_SIZE
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#
# # Set up the clock
# clock = pygame.time.Clock()
#
# displayMenu(screen)
# setZeroList(tempGen)
# setInitialPatternList(tempGen)
# copyList(tempGen, currentGen)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:
#                 setZeroList(tempGen)
#                 setInitialPatternList(tempGen)
#                 copyList(tempGen, currentGen)
#             elif event.key == pygame.K_q:
#                 pygame.quit()
#                 quit()
#
#     displayList(screen, currentGen)
#     displayMenu(screen)
#
#     pygame.display.update()
#     clock.tick(30)


# import keyboard
# import random
# import time
#
# MAX_ROW = 30
# MAX_COL = 60
#
# currentGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
# tempGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
#
#
# def displayMenu():
#     print("[P]lay – Press 'P' to play.")
#     print("[Q]uit – Press 'Q' to exit.")
#
#
# def displaySubMenu():
#     print("[S]top – Press 'S' to stop.")
#
#
# def setZeroList(lst):
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             lst[row][col] = 0
#
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
#
# def copyList(src, dest):
#     for row in range(len(src)):
#         for col in range(len(src[0])):
#             dest[row][col] = src[row][col]
#
#
# # def displayList(lst):
# #     cell_size = 10
# #     for row in lst:
# #         for col in range(len(lst[0])):
# #             if lst[row][col] == 1:
# #                 color = (0, 0, 0)
# #             else:
# #                 color = (0, 255, 0)
# #         print(' '.join([str(col) for col in row]))
# def displayList(screen, lst):
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             x = col * CELL_SIZE
#             y = row * CELL_SIZE
#             if lst[row][col] == 1:
#                 color = (0, 255, 0)  # green
#             else:
#                 color = (0, 0, 0)  # black
#             pygame.draw.rect(screen, color, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
#
#
# def countNeighbors(lst, row, col):
#     count = 0
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j == 0:
#                 continue
#             if row + i < 0 or row + i >= MAX_ROW or col + j < 0 or col + j >= MAX_COL:
#                 continue
#             if lst[row + i][col + j] == 1:
#                 count += 1
#     return count
#
#
# def setNextGenList(currentGen, tempGen):
#     for row in range(MAX_ROW):
#         for col in range(MAX_COL):
#             count = countNeighbors(currentGen, row, col)
#             if currentGen[row][col] == 1:
#                 if count < 2 or count > 3:
#                     tempGen[row][col] = 0
#                 else:
#                     tempGen[row][col] = 1
#             else:
#                 if count == 3:
#                     tempGen[row][col] = 1
#                 else:
#                     tempGen[row][col] = 0
#
#
# displayMenu()
# setZeroList(tempGen)
# setInitialPatternList(tempGen)
# displayList(currentGen)
# copyList(tempGen, currentGen)
#
# while True:
#     choice = input("Enter your choice: ")
#     if choice.upper() == 'P':
#         while True:
#             displaySubMenu()
#             setNextGenList(currentGen, tempGen)
#             copyList(tempGen, currentGen)
#             displayList(currentGen)
#
#             if keyboard.is_pressed('s'):
#                 setZeroList(tempGen)
#                 setInitialPatternList(tempGen)
#                 copyList(tempGen, currentGen)
#                 displayList(currentGen)
#                 break
#             elif keyboard.is_pressed('q'):
#                 sys.exit()
#     elif choice.upper() == 'Q':
#         sys.exit()
#     else:
#         print("Invalid choice, try again.")

# while True:
#     choice = input("Enter your choice: ")
#     if choice.upper() == 'P':
#         while True:
#             displaySubMenu()
#             setNextGenList(currentGen, tempGen)
#             copyList(tempGen, currentGen)
#             # displayList(currentGen)
#
#             # if keyboard.is_pressed('p'):
#             #     break
#             # elif keyboard.is_pressed('s'):
#             #     setZeroList(tempGen)
#             #     setInitialPatternList(tempGen)
#             #     copyList(tempGen, currentGen)
#             #     displayList(currentGen)
#             # elif keyboard.is_pressed('q'):
#             #     sys.exit()
#
#             if keyboard.is_pressed('s'):
#                 setZeroList(tempGen)
#                 setInitialPatternList(tempGen)
#                 copyList(tempGen, currentGen)
#                 displayList(currentGen)
#                 break
#             elif keyboard.is_pressed('q'):
#                 sys.exit()




# import random
# import time
# import sys
# # import keyboard
#
# MAX_ROW = 30
# MAX_COL = 60
#
# currentGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
# tempGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
#
#
# def displayMenu():
#     print("[P]lay – Press 'P' to play.")
#     print("[Q]uit – Press 'Q' to exit.")
#
#
# def displaySubMenu():
#     print("[S]top – Press 'S' to stop.")
#
#
# def setZeroList(lst):
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             lst[row][col] = 0
#
#
# def setInitialPatternList(lst):
#     while True:
#         row = random.randint(0, MAX_ROW - 6)
#         col = random.randint(0, MAX_COL - 7)
#         pattern = [[0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 1],
#                    [0, 1, 1, 0, 0, 0, 0],
#                    [0, 0, 1, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 1, 1, 0],
#                    [0, 0, 0, 1, 1, 0, 0]]
#         valid_pattern = True
#         for i in range(6):
#             for j in range(7):
#                 if lst[row+i][col+j] == 1 and pattern[i][j] == 1:
#                     valid_pattern = False
#                     break
#             if not valid_pattern:
#                 break
#         if valid_pattern:
#             break
#
#     for i in range(6):
#         for j in range(7):
#             if pattern[i][j] == 1:
#                 lst[row+i][col+j] = 1
#
#
# def copyList(src, dest):
#     for row in range(len(src)):
#         for col in range(len(src[0])):
#             dest[row][col] = src[row][col]
#
#
# def displayList(lst):
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             if lst[row][col] == 1:
#                 print('\u2588', end='')
#             else:
#                 print(' ', end='')
#         print()
#
#
# def countNeighbors(lst, row, col):
#     count = 0
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j == 0:
#                 continue
#             if row + i < 0 or row + i >= MAX_ROW or col + j < 0 or col + j >= MAX_COL:
#                 continue
#             if lst[row + i][col + j] == 1:
#                 count += 1
#     return count
#
#
# def setNextGenList(currentGen, tempGen):
#     setZeroList(tempGen)
#     for row in range(MAX_ROW):
#         for col in range(MAX_COL):
#             count = countNeighbors(currentGen, row, col)
#             if currentGen[row][col] == 1:
#                 if count < 2 or count > 3:
#                     tempGen[row][col] = 0
#                 else:
#                     tempGen[row][col] = 1
#             else:
#                 if count == 3:
#                     tempGen[row][col] = 1
#                 else:
#                     tempGen[row][col] = 0
#
# while True:
#     choice = input("Enter your choice: ")
#     if choice.upper() == 'P':
#         while True:
#             displaySubMenu()
#             setNextGenList(currentGen, tempGen)
#             copyList(tempGen, currentGen)
#             displayList(currentGen)
#
#             if keyboard.is_pressed('s'):
#                 setZeroList(tempGen)
#                 setInitialPatternList(tempGen)
#                 copyList(tempGen, currentGen)
#                 displayList(currentGen)
#                 break
#             elif keyboard.is_pressed('q'):
#                 sys.exit()
#     elif choice.upper() == 'Q':
#         sys.exit()
#     else:
#         print("Invalid choice, try again.")

import random
import time

MAX_ROW = 30
MAX_COL = 60

currentGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]
tempGen = [[0 for col in range(MAX_COL)] for row in range(MAX_ROW)]

def displayMenu():
    print("[P]lay – Press 'P' to play.")
    print("[Q]uit – Press 'Q' to exit.")

def displaySubMenu():
    print("[S]top – Press 'S' to stop.")

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

def getNeighbors(lst, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            r = (row + i + MAX_ROW) % MAX_ROW
            c = (col + j + MAX_COL) % MAX_COL
            count += lst[r][c]
    count -= lst[row][col]
    return count

def setNextGenList():
    global currentGen, tempGen
    setZeroList(tempGen)
    for row in range(MAX_ROW):
        for col in range(MAX_COL):
            n = getNeighbors(currentGen, row, col)
            if currentGen[row][col] == 1 and n < 2:
                tempGen[row][col] = 0
            elif currentGen[row][col] == 1 and (n == 2 or n == 3):
                tempGen[row][col] = 1
            elif currentGen[row][col] == 1 and n > 3:
                tempGen[row][col] = 0
            elif currentGen[row][col] == 0 and n == 3:
                tempGen[row][col] = 1
    copyList(tempGen, currentGen)

displayMenu()
setZeroList(tempGen)
setInitialPatternList(tempGen)
copyList(tempGen, currentGen)
displayList(currentGen)

while True:
    choice = input("Enter your choice: ")
    if choice.upper() == 'P':
        while True:
            displaySubMenu()
            setNextGenList()
            displayList(currentGen)
            time.sleep(0.1)
            if input("Press any key to continue, or 'S' to stop: ").upper() == 'S':
                setZeroList(tempGen)
                setInitialPatternList(tempGen)
                copyList(tempGen, currentGen)
                displayList(currentGen)
                break
    elif choice.upper() == 'Q':
        print("\nThank you for playing my 1st version of Game of Life")
        break
