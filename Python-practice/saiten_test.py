s = input().rstrip().split(' ')
n = int(s[0])
m = int(s[1])
c = [input().split() for l in range(n)]

for i in range(n):
    a = int(c[i][0])
    b = int(c[i][1])
    if a-(b*5) < 0:
        d = 0
    else:
        d = a-(b*5)
    if d >= m:
        print(str(i+1))
