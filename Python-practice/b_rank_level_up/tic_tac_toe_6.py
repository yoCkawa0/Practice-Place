# result = "D"
# a = []

# for i in range(5):
#     a.append(input())

# # 横
# for i in range(5):
#     c = 0
#     cri = a[i][0]

#     for s in a[i]:
#         if s != "." and s == cri:
#             c += 1
#         else:
#             break
#     if c == 5:
#         result = cri

# if result == "D":
#     # 縦
#     cri = a[0]
#     for i in range(5):
#         c = 0
#         tmp = a[i]
#         for n in range(5):
#             if a[n][i] != "." and a[n][i] == cri[i]:
#                 c += 1
#         if c == 5:
#             result = cri[i]

# if result == "D":
#     # 斜め
#     cri1 = a[0][0]
#     cri2 = a[0][4]
#     c1 = 0
#     c2 = 0
#     for i in range(5):
#         if cri1 != "." and cri1 == a[i][i]:
#             c1 += 1
#         if cri2 != "." and cri2 == a[i][4-i]:
#             c2 += 1

#         if c1 == 5:
#             result = cri1
#         if c2 == 5:
#             result = cri2

# print(result)

board = []

for i in range(5):
    board.append(input())


def row():
    result = "D"

    for line in board:
        pivot = line[0]
        count = 0

        for stone in line:
            if stone != "." and stone == pivot:
                count += 1
            else:
                break

        if count == 5:
            result = pivot
            break

    return result


def column():
    result = "D"

    for i in range(5):
        pivot = ""
        count = 0

        for j in range(5):
            if pivot == "":
                pivot = board[j][i]

            stone = board[j][i]
            if stone != "." and stone == pivot:
                count += 1
            else:
                break

        if count == 5:
            result = pivot
            break

    return result


def oblique():
    result = "D"
    direction = [True, False]

    for reverse in direction:
        pivot = ""
        count = 0

        if reverse:
            j = 0
            j_diff = 1
        else:
            j = 4
            j_diff = -1

        for i in range(5):

            stone = board[i][j]

            if pivot == "":
                pivot = stone

            if stone != "." and stone == pivot:
                count += 1

            j = j + j_diff

        if count == 5:
            result = pivot
            break

    return result


row = row()
column = column()
oblique = oblique()

if row != "D":
    print(row)
elif column != "D":
    print(column)
elif oblique != "D":
    print(oblique)
else:
    print("D")
