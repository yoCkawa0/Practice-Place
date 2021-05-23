# coding: utf-8
# a = int(input())
# for i in range(a):
#     if i != a-1:
#         # print("paiza",end="\n")
#         print("test", end=" ")
#     else:
#         print("test", end="")
# print(" ")


# num = int(input())

# a = []
# while True:
#     # line = input()
#     if input() == "":
#         break
#     a.append(input().split(" "))
#     # a.append(input())
# print(a)
# for item in a:
#     # print(item.split(' '))
#     print(item, end=" ")


# n = int(input())

# a = input().split()
# print(a)
# for i in range(n):
#     print(a[i])


n = int(input())
a = []
for i in range(n):
    a.append(input().split(" "))
    a[i][1] = int(a[i][1]) + 1

for j in range(n):
    print(j)

# for j in range(n):
#     for m in range(n):
#         print(j)
#         print(m)

#         print(a[j][m])
