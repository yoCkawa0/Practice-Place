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
    print(p)
    print(a)
    # print("--------")
    # print(p)
    # print(a)
    d[p] = int(a) + int(d[p])

l = input()
print(d[l])

#
n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split()
    a = int(a)
    dmg[p] += a

names = list(dmg.keys())
names.sort()

for name in names:
    print(dmg[name])

#
[p, q, r] = [int(i) for i in input().split()]
AB = {}
BC = {}

for _ in range(p):
    [i, j] = [int(n) for n in input().split()]
    AB[i] = j

for _ in range(q):
    [j, k] = [int(n) for n in input().split()]
    BC[j] = k

AC = {}

for i in range(1, p + 1):
    AC[i] = BC[AB[i]]

for i, k in AC.items():
    print(i, k)

#
n = int(input())
[a, b] = input().split()
a = int(a)
b = int(b)

p = 1
k = 1
c = 0

while n >= k:
    k += p*a
    p += k % b
    c += 1


print(c)
# print(n)
# print(a)
# print(b)

#
H = int(input())
n = 0
pd1 = 1
pd2 = 1
pd3 = 1
md1 = 1
md2 = 1
md3 = 1
p = 0


while p != 1:
    # n += 1
    n += 1
    if n == 1 or n == 2:
        H -= 1
        print(n)
        print("与えたd"+str(pd1))
        print("受けたd"+str(md1))
        print("------------")
        print(H)
        print("------------")
        print("------------")

    else:
        # 与えるd
        # md1 + md2
        pd3 = pd2
        pd2 = pd1
        pd1 = md1 + md2
        # print(pd1)
        # print(pd2)
        print(n)
        print("与えたd"+str(pd1))

        # 受けるd
        md3 = md2
        md2 = md1
        md1 = (pd2*2) + pd3
        H -= md1
        print("受けたd"+str(md1))
        print("------------")
        print(H)
        print("------------")
        print("------------")
        if H <= 0:
            p = 1

        # print(H)
print(n)

#
n = int(input())
num = 0
for i in range(n):
    [l, k] = input().split()
    l = int(l)
    k = int(k)

    if l == k:
        num += l*k
    else:
        num += l+k
print(num)

#
pattern = input()
string = input()
result = 0

for i in range(len(string) - len(pattern) + 1):
    portion = string[i: i + len(pattern)]

    if portion == pattern:
        result += 1

print(result)

#
num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    inputs[int(tmp[1])] = tmp[0]

inputs = sorted(inputs.items())

for i in inputs:
    print(i[1])

#
n = input()
s = n[0]
tmp = s
for i in range(1, 5):
    if n[i] != s or n[i] == ".":
        tmp = "D"
        break
print(tmp)

#
for i in range(5):
    n = input()
    s = n[0]
    tmp = s
    for l in range(1, 5):
        print("------")
        print(l)
        print(tmp)

        if n[l] != s or n[l] == ".":
            tmp = "D"
        if tmp == s:
            break
print(tmp)

#
for i in range(5):
    n = input()
    s = n[0]
    tmp = "D"
    c = 0
    for l in range(1, 5):
        if n[l] == s:
            c += 1
    if c == 4:
        tmp = s
        break
print(tmp)

#

n = input()
m = n.replace(' ', '')
a = list(m)

b = []
for i in range(len(a)):
    c = ord(a[i]) - 96
    b.append(c)
print(b)
# print(len(b))

d = []
for i in range(len(b)-1):
    c = b[i] + b[i+1]
    d.append(c)
# d = []
print(d)
