import time

s = input().rstrip().rsplit()
a = int(s[0])
b = int(s[1])
c = int(s[2])
n = int(input())
s = [input().split() for l in range(n)]
# =================
dead = 8*60+59
d = 539 - b - c

maxs = 0
for i in range(n):
    hour = int(s[n-i-1][0])
    minu = int(s[n-i-1][1])
    deadi = hour * 60 + minu
    # print("deadi = "+str(deadi))
    if d >= deadi:
        maxs = deadi
maxs -= a
hour = (maxs)//60
minu = (maxs)-(hour*60)
print("0"+str(hour)+":"+str(minu))
