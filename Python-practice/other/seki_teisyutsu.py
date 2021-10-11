# 入力を格納
# スペースで分けてsに格納
s = input().rstrip().split(' ')
# print(s)
# n 座先数
n = int(s[0])
# m グループ数
m = int(s[1])
# s[2]からs[]
c = [input().split() for l in range(m)]
# 座席を準備
o = [0] * n

for x in range(m):
    # a = グループの人数
    a = int(c[x][0])

    # b = 席の始点
    b = int(c[x][1])

    # フラグ k
    k = 0

    d = 0
    for y in range(a):
        if (b+y-1) >= n:
            d = (b + y - 1) - (n-1)
        else:
            d = (b + y - 1)

        if o[d] == 0:
            k = 1
        else:
            k = 0
            break

    if k == 1:
        for z in range(a):
            if (b+z-1) >= n:
                d = (b + z - 1) - (n)
                # print("オーバーフロー:"+str(d))
            else:
                d = (b + z - 1)

            o[d] = 1
print(o.count(1))
