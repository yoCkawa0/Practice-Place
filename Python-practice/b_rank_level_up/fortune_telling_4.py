s = input()
n = int(input())
dic = {}
for i in range(n):
    tmp = input().split()
    dic[tmp[0]] = tmp[1]


print(dic[s])
