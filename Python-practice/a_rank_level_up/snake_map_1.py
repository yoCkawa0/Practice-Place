# tmp = input().split()
# h = int(tmp[0])
# w = int(tmp[1])
# n = int(tmp[2])

# b = []
# for i in range(h):
#     b.append(input())
# for i in range(n):
#     tmp = input().split()
#     y = int(tmp[0])
#     x = int(tmp[1])
#     print(b[y][x])


h, w, n = map(int, input().split())
s = [list(input()) for _ in range(h)]
for _ in range(n):
    y, x = map(int, input().split())
    print(s[y][x])
