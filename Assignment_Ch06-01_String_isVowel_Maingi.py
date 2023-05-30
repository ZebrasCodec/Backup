
# Samuel Maingi
# Assignment 06-01
# 04/03/2023


sntc = input("Write a sentence about something positive that happened to you this week:\n> ")

def isVowel(char):
    vwl = 'aeiouyAEIOUY'
    if char in vwl:
        return True
    else:
        return False
##
#def isVowel(char):
#    vwl = "aeiouyAEIOUY"
#    if char in vwl:
#        return True
#    else:
#        return False
##


def Count(sntc):
    cnt = 0
    for character in sntc:
        if isVowel(character):
            cnt += 1
    result = cnt
    #result = Count(cnt)
    print("\nNumber of vowels in Sentence:",result)


Count(sntc)
