n = int(input())
dic = {}
for i in range(n):
    tmp = input().split()
    dic[tmp[0]] = tmp[1]

for i in dic:
    print(i+" "+dic[i])
