
# Samuel Maingi
# Assignment 06-01
# 04/03/2023

def isVowel(char):
    vwl = 'aeiouyAEIOUY'
    if char in vwl:
        return True
    else:
        return False


def Count(sntc):
    cnt = 0
    for char in sntc:
        if isVowel(char):
            cnt += 1
    result = cnt
    #result = Count(cnt)
    print("\nNumber of vowels in Sentence:",result)


if __name__ == "__main__":
    sntc = input("Write a sentence about something positive that happened to you this week:\n> ")
    Count(sntc)

