# a = [None]*5
# for i in range(5):
#     a[i] = input()
# c = 0
# tmp = ""
# for i in range(5):
#     c = 0
#     tmp = a[0][i]

#     for n in range(5):
#         if c == 4:
#             print(tmp)
#             break
#         if tmp == a[i][n]:
#             c += 1
# if c != 4:
#     print("D")

# =============================

# result = "D"
# a = [None]*5
# for i in range(5):
#     a[i] = input()
# cri = a[0]
# for i in range(5):
#     c = 0
#     tmp = a[i]
#     for n in range(5):
#         if a[n][i] != "." and a[n][i] == cri[i]:
#             c += 1
#     if c == 5:
#         result = cri[i]
#         print(result)
#     else:
#         break

# print(result)

# =============================

# board = []
# result = "D"

# for i in range(5):
#     board.append(input())

# for i in range(5):
#     pivot = ""
#     count = 0

#     for j in range(5):
#         stone = board[j][i]

#         if pivot == "":
#             pivot = stone

#         if stone != "." and stone == pivot:
#             count += 1
#         else:
#             break

#     if count == 5:
#         result = pivot
#         break


# print(result)

# =============================

result = "D"
a = []
for i in range(5):
    a.append(input())
cri = a[0]
# print("----------")
for i in range(5):
    c = 0
    tmp = a[i]
    # print(tmp)
    for n in range(5):
        if a[n][i] != "." and a[n][i] == cri[i]:
            c += 1
    if c == 5:
        result = cri[i]
print(result)
