# 入力を格納
# スペースで分けてsに格納
s = input().rstrip().split(' ')
print(" ")
print("---------------------")
# print(s)
# n 座先数
n = int(s[0])
print("座席数n:"+s[0])
# m グループ数
m = int(s[1])
print("グループ数m:"+s[1])
print(" ")
print("---------------------")

# s[2]からs[]
c = [input().split() for l in range(m)]
print(c)

# 座席を準備
o = [0] * n
print(" ")
print("----------座席初期状態 o: -----------")
print(o)
print("-------------------------------------")
print(" ")

for x in range(m):
    # a = グループの人数
    a = int(c[x][0])
    print(str(x+1)+"グループ目の人数:"+str(a))

    # b = 席の始点
    b = int(c[x][1])
    print("最初の人が座る席番号:"+str(b)+"番席")

# ここまで　-------------------------------------

    # フラグ k
    k = 0

    d = 0
    for y in range(a):
        print(y)
        print("b+y-1 = "+str(b+y-1))

        if (b+y-1) >= n:
            d = (b + y - 1) - (n-1)
            print("オーバーフロー:"+str(d))
        else:
            d = (b + y - 1)

        if o[d] == 0:
            k = 1
            print("<フラグ>"+str(k))
        else:
            k = 0
            print("<フラグ>"+str(k))
            break

    if k == 1:
        for z in range(a):
            if (b+z-1) >= n:
                d = (b + z - 1) - (n)
                # print("オーバーフロー:"+str(d))
            else:
                d = (b + z - 1)

            o[d] = 1
            print("-------------")
    else:
        print("入店できませんでした。")
        # print(z)
    print("----------現在の座席状態 : -----------")
    print(o)
    print(o.count(1))
    print("人着席しました。")
    print("-------------end")

print("----------最終座席状態 : -----------")
print("----------------------------------")
print(o.count(1))
