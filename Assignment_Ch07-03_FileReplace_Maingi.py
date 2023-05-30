
# Samuel Maingi
# Assignment 07-02
# 04/05/2023

import re

def replace():
    initial_word = input("Enter the word to search for: ")
    word = initial_word.lower()
    name = input(f"Enter text to replace {initial_word} with: ")
    with open("Misc/output.txt", "w") as out_file:
        with open("Misc/data.txt", "r") as in_file:
            for line in in_file:
                line = re.sub(r"\b" + re.escape(word) + r"\b", name.lower(), line, flags=re.IGNORECASE)
                out_file.write(line)
    print("Replacement complete, all changes saved to 'output.txt'")

replace()