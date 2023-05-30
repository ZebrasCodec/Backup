
# Samuel Maingi
# Assignment 08-02
# 05/04/2023

n = 10

MT = [[] for i in range(n)]


i = 0

while i < n:
    j = 0
    while j < n:
        MT[i].append(0)
        j += 1
    i += 1

i = 0
while i < n:
    j = 0
    while j < n:
        if i == 0 and j == 0:
            MT[i][j] = 1
        elif i == 0:
            MT[i][j] = j + 1
        elif j == 0:
            MT[i][j] = i + 1
        else:
            MT[i][j] = (i + 1) * (j + 1)
        j += 1
    i += 1

print("x", end="\t")
for i in range(1, n+1):
    print(i, end="\t")
print()

for i in range(1, n+1):
    print(i, end="\t")
    for j in range(1, n + 1):
        print(MT[i-1][j-1], end="\t")
    print()
