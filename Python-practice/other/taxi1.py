import math

s = input().rstrip().split(' ')
# 種類
n = int(s[0])
# 距離
m = int(s[1])
# print("")
# print("移動距離:"+str(m))

c = [input().split() for l in range(n)]
# print(c)

#
# 600 200 200 400
# 900 800 400 500
# ai bi ci di

# 計算式
# bi + (int((m - ai) / ci)) * di
# 四捨五入　マイナス時も考える。
# round(f, 0)

# 最大料金
maxf = 0
# 最小料金
minf = 10000

for i in range(n):
    # print(str(i+1)+"種類目")
    # 初乗り距離
    ai = int(c[i][0])
    # 初乗り運賃
    bi = int(c[i][1])
    # 加算距離
    ci = int(c[i][2])
    # 加算運賃
    di = int(c[i][3])

    # 条件考え直し
    if (m - ai) < 0:
        fee = bi
    else:
        f = int(float((m - ai) // ci)) + 1
        fee = bi + (di * f)
    # if m - ai < 0:
    #     fee = bi
    #     k = 1
    # elif ((m - ai) // ci > 0) and ((m - ai) / ci != 0):
    #     fee = bi + (((m - ai) // ci) + 1) * di
    #     k = 2
    # elif (m - ai) == ci:
    #     # fee = bi + ((m - ai) // ci) * di
    #     fee = bi + (((m - ai) // ci) + 1) * di
    #     k = 3
    # elif (m - ai) // ci == 0:
    #     fee = bi + di
    #     k = 4

    # -----------------------

    # print((math.ceil((m - ai) / ci)))
    # 料金
    # if (math.ceil((m - ai) / ci)) > 0:
    #     fee = bi + (math.ceil((m - ai) / ci)) * di
    # elif (math.ceil((m - ai) / ci)) == 0:
    #     fee = bi + di
    # else:
    #     fee = bi

    if maxf < fee:
        maxf = fee
        # maxk = k
    if minf > fee:
        minf = fee
        # mink = k
    # print(round(((m - ai) / ci), 0))
    # print(math.ceil((m - ai) / ci))
#     print(fee)


# print("------------------")
# print("最大")
# print(maxf)
# print(maxk)
# print("最小")
# print(minf)
# print(mink)

print(minf, end=" ")
print(maxf)

g = int(5.5 - 2.0)
h = float(1000 // 3)
i = int(h)
print(g)
print(h)
print(i)
