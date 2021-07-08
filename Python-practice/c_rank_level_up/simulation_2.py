n = int(input())

l = input().split(" ")
a = int(l[0])
b = int(l[1])

an = 1
bn = 1
c = 0

while bn <= n:
    bn += (a * an)
    an += (bn % b)
    c += 1


print(c)
