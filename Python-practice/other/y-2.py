# # from day2 import S

# n = int(input())
# a = [0]*n
# b = input().split()
# for i in range(n):

#     a[i] = int(b[i])

# # print(a)

# q = int(input())

# for i in range(q):
#     c = input().split()
#     qe = int(c[0])

#     if qe == 1:
#         num = int(c[1])-1
#         a[num] = int(c[2])

#     else:
#         # qe == 2の場合
#         l = int(c[1])
#         r = int(c[2])

#         s = int(c[3])
#         t = int(c[4])
#         pc = 0

#         for m in range(l-1, r-1):
#             if s <= a[m] and a[m] <= t:
#                 pc += 1
#         print(pc)

#
m = input().split()
n = int(m[0])
k = int(m[1])

s = input()
s = list(s)
cp = 0
pcp = 0

for i in range(n):
    pcp = cp

    for l in range(k):
        if s[l] == "S":
            s[l] = "."
            if l == 0:
                s[l+1] = "."

            elif l != (len(s)-1):
                s[l-1] = "."
            else:
                s[l+1] = "."
                s[l-1] = "."

    cp = s.count(".")
    if pcp > cp:
        cp = pcp
print(cp)
