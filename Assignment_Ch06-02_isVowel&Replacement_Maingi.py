# Samuel Maingi
# Assignment 06-01
# 04/03/2023

# def isVowel(char):
#     vwl = "aeiouyAEIOUY"
#     if char in vwl:
#         return True

from Assignment_Ch06_02_Function_File import isVowel

if __name__ == '__main__':
    sntc = input(" WRITE a sentence about something "
                 "positive that happened to you this week:\n> ")

    new = ""
    for let in sntc:
        if isVowel(let):
            new += "*"
        else:
            new += let

    print("\n", new)
