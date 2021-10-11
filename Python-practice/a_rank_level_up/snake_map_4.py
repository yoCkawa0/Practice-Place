h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for n in range(w):
        if i == 0:
            if s[i+1][n] == "#":
                print(i, n)
        elif i == h-1:
            if s[i-1][n] == "#":
                print(i, n)
        else:
            if s[i+1][n] == "#" and s[i-1][n] == "#":
                print(i, n)
