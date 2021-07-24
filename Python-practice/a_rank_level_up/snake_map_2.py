# h, w, n = map(int, input().split())

# b = []
# for _ in range(h):
#     b.append(input())

# for i in range(n):
#     y, x = map(int, input().split())
#     # print(b[y][x])
#     b[y] = b[y][:x]+"#"+b[y][x+1:]
#     # print(b[y][x])

# for i in range(h):
#     print(b[i])

h, w, n = map(int, input().split())
s = [list(input()) for _ in range(h)]

for _ in range(n):
    y, x = map(int, input().split())
    s[y][x] = "#"

for y in range(h):
    print("".join(s[y]))
