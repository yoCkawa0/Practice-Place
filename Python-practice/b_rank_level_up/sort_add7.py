# num = int(input())
# inputs = {}
# result = {}

# for i in range(num):
#     tmp = input().split()

#     exist = False
#     for (key, value) in inputs.items():
#         if key == tmp[0]:
#             exist = True

#     if exist:
#         inputs[tmp[0]] = inputs[tmp[0]] + int(tmp[1])
#     else:
#         inputs[tmp[0]] = int(tmp[1])

# # ソート用にkeyとvalueを反転させた辞書を作る
# for (key, value) in inputs.items():
#     result[value] = key

# result = sorted(result.items(), reverse=True)

# for i in result:
#     print(i[1] + " " + str(i[0]))

n = int(input())
dic = {}
for i in range(n):
    inputs = input().split()
    strs = inputs[0]
    num = int(inputs[1])

    if strs in dic:
        dic[strs] += num
    else:
        dic[strs] = num
dic2 = sorted(dic.items(), reverse=True, key=lambda x: x[1])
# print(dic)
for i in dic2:
    print(i[0] + " " + str(i[1]))
