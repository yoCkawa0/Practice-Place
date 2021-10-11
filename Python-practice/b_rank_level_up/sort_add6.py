n = int(input())
k = input().split()
l = [0]*n

for i in range(n):
    l[i] = int(k[i])
l.sort()

for i in l:
    print(i)
