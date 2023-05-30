
# Samuel Maingi
# Assignment 06-03
# 04/05/2023


def isPalindrome(word2):
    return word2 == word2[::-1]


while True:
    word = input("Please enter a word (QUIT to stop): ")
    word2 = word
    word2 = word.lower()

    if word2 in ["quit", "q", "exit", "/end"]:
        print("Thanks for using the palindrome checker. Goodbye!")
        break

    if isPalindrome(word2):
        print(f"\n\tYes, {word} is a palindrome!")
    else:
        print(f"\n\tNo, {word} is not a palindrome.")




