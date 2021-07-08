# プログラムカウンターs
l = 0

# 入力を格納
input_line = input()
# スペースで分けてsに格納
s = input_line.rstrip().split(' ')
print(" ")
print("---------------------")
# print(s)
# n 座先数
n = int(s[0])
# m グループ数
m = int(s[1])
print("m:"+s[1])

# s[2]からs[]
c = [input().split() for l in range(m)]
print(c)
# 座席を準備
o = [0] * n
print(o)


# x y
for x in range(m):
    # for y in range(2):
    # a = 人数
    a = int(c[x][0])
    print(x)
    print(a)
    # b = 席の始点
    b = int(c[x][1])
    print(b)
    # 空席判定
    if o[b-1] == 0:
        # ↑これいるのか？
        k = 0
        for y in range(a-1):
            if o[b+y-1] == 0:
                k = 1
                # o[b+y-1] = 1
            else:
                k = 0

        if k == 1:
            for z in range(a-1):
                o[b+z-1] = 1
                print("-------------")
                print(z)
                print(o)
        # else:
        #     break

        # プログラムカウンタに加算
        l += 1

    # else:
    #     # print("NG")
    #     break

# print(n)
# print(m)

# 着席できたグループ数
# print(l)
print(o)

print(o.count(1))
