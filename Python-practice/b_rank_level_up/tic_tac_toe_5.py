result = "D"
a = []

for i in range(5):
    a.append(input())
cri1 = a[0][0]
cri2 = a[0][4]
c1 = 0
c2 = 0
for i in range(5):
    if cri1 != "." and cri1 == a[i][i]:
        c1 += 1
    if cri2 != "." and cri2 == a[i][4-i]:
        c2 += 1

    if c1 == 5:
        result = cri1
    if c2 == 5:
        result = cri2
print(result)

# board = []
# result = "D"
# direction = [True, False]

# for i in range(5):
#     board.append(input())

# for reverse in direction:
#     pivot = ""
#     count = 0

#     if reverse:
#         j = 0
#         j_diff = 1
#     else:
#         j = 4
#         j_diff = -1

#     for i in range(5):

#         stone = board[i][j]

#         if pivot == "":
#             pivot = stone

#         if stone != "." and stone == pivot:
#             count += 1

#         j = j + j_diff

#     if count == 5:
#         result = pivot
#         break

# print(result)
