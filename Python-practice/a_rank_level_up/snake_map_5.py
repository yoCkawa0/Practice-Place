# h, w = map(int, input().split())
# s = [list(input()) for _ in range(h)]

# for i in range(h):
#     for n in range(w):
#         if i == 0:
#             if n == 0:
#                 # 右　下
#                 if s[i][n+1] == "#" and s[i+1][n] == "#":
#                     print(i, n)
#             elif n == w-1:
#                 # 左　下
#                 if s[i][n-1] == "#" and s[i+1][n] == "#":
#                     print(i, n)
#             else:
#                 # 右　下　左
#                 if s[i][n+1] == "#" and s[i+1][n] == "#" and s[i+1][n] == "#":
#                     print(i, n)

#         elif i == h-1:
#             if n == 0:
#                 # 右　上
#                 if s[i][n+1] == "#" and s[i-1][n] == "#":
#                     print(i, n)
#             elif n == w-1:
#                 # 左　上
#                 if s[i][n-1] == "#" and s[i-1][n] == "#":
#                     print(i, n)
#             else:
#                 # 右　上　左
#                 if s[i][n+1] == "#" and s[i-1][n] == "#" and s[i+1][n] == "#":
#                     print(i, n)

#         else:
#             if n == 0:
#                 # 右　上　下
#                 if s[i][n+1] == "#" and s[i-1][n] == "#" and s[i+1][n] == "#":
#                     print(i, n)

#             elif n == w-1:
#                 # 上　左　下
#                 if s[i-1][n] == "#" and s[i][n-1] == "#" and s[i+1][n] == "#":
#                     print(i, n)

#             else:
#                 # 右　上　左　下
#                 if s[i][n+1] == "#" and s[i-1][n] == "#" and s[i][n-1] == "#" and s[i+1][n] == "#":
#                     print(i, n)

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        flag_row = False
        flag_column = False

        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                flag_row = True

        if y == 0 or s[y - 1][x] == "#":
            if y == h - 1 or s[y + 1][x] == "#":
                flag_column = True

        if flag_column and flag_row:
            print(y, x)
