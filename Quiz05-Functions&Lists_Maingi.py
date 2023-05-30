
# Samuel Maingi
# Quiz 05
# 03/24/2023

#Question 1

# def result(x):
#     print(x)
#     return len(x)
#
# str = "Hello, world!"
# len = result(str)
# print(f"The length of '{str}' is {len}.")


# # Question 2

# def result(lst):
#     print(lst)
#     x = 5
#     y = 7
#     return x, y
#
# lst = input("Input 5 Random digits (seperated by a space): ")
# x, y = result(lst)
# print("x =",x)
# print("y =",y)


# # Question 3
def concation(a, b, c, d, e):
    return str(a) + str(b) + str(c) + str(d) + str(e)

num1 = int(input("Enter a digit: "))
num2 = int(input("Enter a digit: "))
num3 = int(input("Enter a digit: "))
num4 = int(input("Enter a digit: "))
num5 = int(input("Enter a digit: "))

result = concation(num1, num2, num3, num4, num5)
print(result)
