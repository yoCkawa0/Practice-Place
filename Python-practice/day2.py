num = input().rstrip().split(":")

h = int(num[0])
m = int(num[1])

if m + 30 >= 60:
    m = m + 30 - 60
    h += 1
else:
    m += 30

if len(str(h)) == 1:
    print("0"+str(h), end=":")
else:
    print(str(h), end=":")

if len(str(m)) == 1:
    print("0"+str(m))
else:
    print(str(m))

#
S = input()
h = int(S[:2])
m = int(S[3:])

if m + 30 >= 60:
    h = str(h + 1)
    m = str(m + 30 - 60)
else:
    h = str(h)
    m = str(m + 30)

if len(h) == 1:
    h = "0" + h
if len(m) == 1:
    m = "0" + m

print(h + ":" + m)

#
n = int(input())
for i in range(n):
    time = input().rstrip().split(" ")
    t = time[0]
    h = int(t[:2])
    m = int(t[3:5])
    ah = int(time[1])
    am = int(time[2])
    print("")
    print("-------------")
    print(m)
    print(am)
    print(h)
    print(ah)
    if m + am >= 60:
        ah += 1
        m = m + am - 60
        print(m)
    else:
        m += am
        print(m)

    if h + ah >= 24:
        h = h + ah - 24
        print(h)
    else:
        h += ah
        print(h)

    if len(str(h)) == 1 and len(str(m)) == 1:
        print("0"+str(h)+":"+"0"+str(m))
    elif len(str(h)) == 1 and len(str(m)) != 1:
        print("0"+str(h)+":"+str(m))
    elif len(str(h)) != 1 and len(str(m)) == 1:
        print(str(h)+":"+"0"+str(m))
    else:
        print(str(h)+":"+str(m))

#
n = int(input())

a = [0] * n

for i in range(n):
    a[i] = input()

k = input()

for i in range(n):
    if a[i] == k:
        print(i + 1)
        break
#

n = int(input())
ab = [None] * n

for i in range(n):
    [a, b] = input().split()
    a = int(a)
    b = int(b)
    ab[i] = [a, b]

ab.sort(reverse=True)

for i in range(n):
    [a, b] = ab[i]
    print(a, b)

#
n = int(input())
gs = [None] * n

for i in range(n):
    [g, s] = input().split()
    g = int(g)
    s = int(s)
    gs[i] = [s, g]

gs.sort(reverse=True)

for i in range(n):
    [s, g] = gs[i]
    print(g, s)

#
n = int(input())
zaisan = {}

for i in range(n):
    [s, a] = input().split()
    zaisan[s] = a

S = input()

print(zaisan[S])

#
n = int(input())
d = {}

for i in range(n):
    [p] = input().split()
    d[p] = 0
# print(d)

m = int(input())
for i in range(m):
    [p, a] = input().split()
    # print("--------")
    # print(p)
    # print(a)
    d[p] = int(a) + int(d[p])

l = input()
print(d[l])
