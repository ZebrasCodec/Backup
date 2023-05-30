
# Samuel Maingi
# Assignment 05-01
# 03/29/2023



while True:
    even = 0
    odd = 0
    nums = input("Enter 10 integers (separated by spaces): ").split()
    for num in nums:
        num = int(num)
        print(num)

        if num % 2 == 0:
            even += num
        else:
            odd += num

    print("\nEven sum:", even)
    print("Odd sum:", odd)

    repeat = input("\nDo you wish to repeat the program? (y/n): ")
    if repeat == "n":
        break


#same thing as above only with random inputs instead of user inp (be sure to comment code not in use)
# import random
#
# even = 0
# odd = 0
#
# while True:
#     for i in range(10):
#         num = random.randint(0, 10)
#         print(num)
#
#
#         if num % 2 == 0:
#             even += num
#         else:
#             odd += num
#
#     print("\nEven sum:", even)
#     print("Odd sum:", odd)
#
#     repeat = input("\nDo you wish to repeat the program? (y/n): ")
#     if repeat == "n":
#         break