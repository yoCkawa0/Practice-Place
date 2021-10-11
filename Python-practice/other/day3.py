# a = [None]*5
# C = "D"
# for i in range(5):
#     n = input()
#     a[i] = n
# # print(a)
# for i in range(0, 5):
#     c = 0
#     for n in range(1, 5):
#         if a[i][n] == ".":
#             break
#         elif a[0][i] == a[n][i]:
#             c += 1

#         if c == 4:
#             # print(i)
#             print(a[0][i])
#             break
# if c != 4:
#     print(C)

#
board = []
result = "D"

for i in range(5):
    board.append(input())

for i in range(5):
    pivot = ""
    count = 0

    for j in range(5):
        stone = board[j][i]

        if pivot == "":
            pivot = stone

        if stone != "." and stone == pivot:
            count += 1
        else:
            break

    if count == 5:
        result = pivot
        break


print(result)
