n = int(input())
dic1 = {}

for i in range(n):
    tmp = input().split()
    dic1[tmp[0]] = tmp[1]

m = int(input())
dic2 = {}
for i in range(m):
    tmp = input().split()
    dic2[tmp[0]] = tmp[1]


for i in dic1:
    print(i + dic2[dic1[i]])
