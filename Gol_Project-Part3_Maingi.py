
# Samuel Maingi
# Assignment GOL 03
# 05/05/2023

import random
import os
import time

MAX_ROW = 40
MAX_COL = 80

currentArray = [['O' for col in range(MAX_COL)] for row in range(MAX_ROW)]
tempArray = [['O' for col in range(MAX_COL)] for row in range(MAX_ROW)]

def displayMenu():
    print("[I]nitial – Press 'I' to load the 'U' pattern.")
    print("[P]lay – Press 'P' to play the game.")
    print("[S]top – Press 'S' to stop the game.")
    print("[C]lear – Press 'C' to set the arrays to the dead cells.")
    print("[Q]uit – Press 'Q' to exit the program.")
    print("[1] Pattern 1 – Press '1' to load pattern1.txt.")
    print("[2] Pattern 2 – Press '2' to load pattern2.txt.")
    print("[3] Pattern 3 – Press '3' to load pattern3.txt.")
    print("[T] Custom – Press 'T' to create a custom pattern.")
    print("[A] Save – Press 'A' to save the current live cell pattern.")
    print("[L] Load – Press 'L' to load a saved file.")

def setZeroArray(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            arr[row][col] = 'O'

def setInitialPatternArray(arr):
    row = random.randint(0, MAX_ROW - 6)
    col = random.randint(0, MAX_COL - 7)
    for i in range(6):
        arr[row + i][col] = 'X'
        arr[row + i][col + 6] = 'X'
    for j in range(1, 6):
        arr[row + 5][col + j] = 'X'

def setPatternFromFileArray(arr, filename):
    with open(filename, 'r') as f:
        pattern = f.read().splitlines()
    row = random.randint(0, MAX_ROW - len(pattern))
    col = random.randint(0, MAX_COL - len(pattern[0]))
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == 'X':
                arr[row + i][col + j] = 'X'

def setUserPatternArray(arr):
    while True:
        print("Enter row and column numbers separated by a comma (or type 'done' to finish):")
        user_input = input().lower()
        if user_input == 'done':
            break
        try:
            row, col = user_input.split(',')
            row, col = int(row), int(col)
            if 0 <= row < MAX_ROW and 0 <= col < MAX_COL:
                arr[row][col] = 'X'
            else:
                print("Invalid input! Row and column numbers must be within the range of the array.")
        except ValueError:
            print("Invalid input! Please enter row and column numbers separated by a comma.")

def saveArray(arr):
    while True:
        filename = input("Enter a filename to save the current live cell pattern (or type 'cancel' to cancel): ")
        if filename.lower() == 'cancel':
            break
        try:
            with open(filename, 'w') as f:
                for row in range(len(arr)):
                    for col in range(len(arr[0])):
                        if arr[row][col] == 'X':
                            f.write(f"{row},{col}\n")
                print(f"The current live cell pattern has been saved to {filename}.")
                break
        except:
            print("An error occurred while trying to save the file. Please try again.")

displayMenu()

while True:
    choice = input("Enter your choice: ")
    if choice.upper() == 'P':

        setZeroList(tempGen)
        setInitialPatternList(tempGen)
        copyList(tempGen, currentGen)
        displayList(currentGen)