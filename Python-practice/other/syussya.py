import time

s = input().rstrip().rsplit()
a = int(s[0])
b = int(s[1])
c = int(s[2])
n = int(input())
# print(a)
# print(b)
# print(c)
# print(n)

s = [input().split() for l in range(n)]
# print(s)
# =================
hour = 8
# hour * 60
minu = 59

dead = 8*60+59
print("dead line"+str(dead))
# paiza駅　最終着時間
d = dead - c - b
# 実際のpaiza駅着時間候補
paiza = 540

paizamax = 0
# deadi = 0

for i in range(n):
    hour = int(s[n-i-1][0])
    minu = int(s[n-i-1][1])
    deadi = hour * 60 + minu
    print("deadi = "+str(deadi))
    if deadi < d:
        d = deadi
        paiza = deadi
        if paizamax < paiza:
            paizamax = paiza
    # print(paizamax)

t = paizamax - a
print(t)
# hour = 400 // 60
hour = int(t // 60)
minu = t-hour*60
print("0"+str(hour)+":"+str(minu))
# print(minu)


# 30 30 30
# 6
# 6 00
# 8 25
# 8 35
# 8 45
# 8 55
# 8 59
