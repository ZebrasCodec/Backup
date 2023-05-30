# Samuel Maingi
# Assignment 05-2
# 03/14/2023

n = 10

print("x", end="\t")
for i in range(1, n+1):
    print(i, end="\t")
print()

for i in range(1, n+1):
    print(i, end="\t")
    for j in range(1, n+1):
        print(i*j, end="\t")
    print()


# size = 10
#
# for i in range(1, size+1):
#     for j in range(1, size+1):
#         if i == 1 and j == 1:
#             print("{:4s}".format("x"), end="")
#         elif i == 1:
#             print("{:4d}".format(j), end="")  # print the column label
#         elif j == 1:
#             print("{:4d}".format(i), end="")  # print the row label
#         else:
#             print("{:4d}".format(i*j), end="")  # print the product
#     print()
