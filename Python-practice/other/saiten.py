s = input().rstrip().split(' ')
print(" ")
print("---------------------")
# n 人数
n = int(s[0])
print("人数n:"+s[0])
# m 合格点
m = int(s[1])
print("合格点m:"+s[1])
print(" ")
print("---------------------")

#
c = [input().split() for l in range(n)]
print(c)

for i in range(n):
    # 点数
    a = int(c[i][0])

    # 欠席回数
    b = int(c[i][1])

    if a-(b*5) >= m:
        # print("合格")
        print(str(i+1))
    else:
        print("不合格")
