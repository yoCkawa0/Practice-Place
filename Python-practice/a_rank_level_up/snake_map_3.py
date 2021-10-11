h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
# print(s)
for i in range(h):
    for n in range(w):
        if n == 0:
            if s[i][n+1] == "#":
                print(i, n)
        elif n == w-1:
            if s[i][n-1] == "#":
                print(i, n)
        else:
            if s[i][n-1] == "#" and s[i][n+1] == "#":
                print(i, n)
