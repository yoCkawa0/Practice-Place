import math

s = input().rstrip().split(' ')
n = int(s[0])
m = int(s[1])
c = [input().split() for l in range(n)]

maxf = 0
minf = 5000

for i in range(n):
    ai = int(c[i][0])
    bi = int(c[i][1])
    ci = int(c[i][2])
    di = int(c[i][3])

    if (m - ai) < 0:
        fee = bi
    elif (m - ai) == 0:
        fee = bi + di
    else:
        f = ((m - ai) // ci) + 1
        print(i)
        print(f)
        fee = bi + (di * f)

    if maxf < fee:
        maxf = fee
    if minf > fee:
        minf = fee

print(minf, end=" ")
print(maxf)
