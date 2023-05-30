
# Samuel Maingi
# Quiz 02
# 03/15/2023

#Part 1

# def Nums():
#     result = []
#     for num in range(1, 5000):
#         if num % 3 == 0 and num % 18 == 0 and num % 54 != 0:
#             result.append(num)
#         elif num % 88 == 0:
#             result.append(num)
#     return result
#
# print(Nums())
#
# # Part 2
# print("\n")
#
# def YesNo(num):
#     # for num in range(1, 5000):
#         if num % 3 == 0 and num % 18 == 0 and num % 54 != 0:
#             return True
#         elif num % 88 == 0:
#             return True
#         else:
#             return False
#
# def Nums():
#     result = []
#     for num in range(1, 5000):
#         if YesNo(num):
#             result.append(num)
#     return result
#
# print(Nums())

# Part 3
print("\n")

def YesNo(num):
    if num % 3 == 0 and num % 18 == 0 and num % 54 != 0:
        return True
    elif num % 88 == 0:
        return True
    else:
        return False

for num in range(1, 5000):
    if YesNo(num):
        print(f"The number {num} is divisible by both 3 and 18 but not 54, or is divisible by 88\n")

