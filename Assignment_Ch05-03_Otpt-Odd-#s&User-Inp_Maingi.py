
# Samuel Maingi
# Assignment 05-03
# 03/29/2023

while True:
    import string

    #A
    while True:
        fstdo = input("Enter 2 Positive Numbers between 1 & 10"
                     ", must seperated by a space:"
                      "\nEnter Number:  ").split()
        x = fstdo[0]
        y = fstdo[1]
        while x.isdigit() and y.isdigit():
            break
        else:
            print("Invalid Input.\n"
                  "Please try again.\n")
            continue
        x = int(fstdo[0])
        y = int(fstdo[1])
        if x > 10 or y > 10:
            print("Invalid Input.\n"
                  "Please try again.\n")
            continue
        elif y < x:
            print("**First Number must be LESS than Second Number**\n")
            continue
        else:
            break

    # B outputs list of all odd numbers inbetween and including x & y
    odd = []
    odd_cnt = x
    while odd_cnt <= y:
        if odd_cnt % 2 != 0:
            odd.append(odd_cnt)
        odd_cnt += 1
    print(f"Odd integers between {x} and {y} are:\n",odd)

    # C Shows sum of all even
    even = 0
    even_calc = x
    while even_calc <= y:
        if even_calc % 2 == 0:
            even += even_calc
        even_calc += 1
    print(f"\nSum of even integers between {x} and {y} =",even)

    # D sum of the square of odd numbers between x & y
    sqr = 0
    lst = 0
    while lst < len(odd):
        sqr += odd[lst] ** 2
        lst += 1
    print(f"\nSum of the squares of odd integers between {x} and {y} =",sqr)


    repeat = input("\nDo you wish to repeat the program? (y/n): ")
    if repeat == "n":
        break


