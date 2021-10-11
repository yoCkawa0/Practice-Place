s = input().rstrip().rsplit()
a = int(s[0])
b = int(s[1])
c = int(s[2])
n = int(input())
s = [input().split() for l in range(n)]
dead = 8*60+59
d = dead - c - b
paiza = 540
paizamax = 0
deadi = 0
for i in range(n):
    hour = int(s[i][0])
    minu = int(s[i][1])
    deadi = hour * 60 + minu
    if deadi < d:
        paiza = deadi
        if paizamax < paiza:
            paizamax = paiza
hour = (paizamax - a)//60
minu = (paizamax - a)-(hour*60)
print("0"+str(hour)+":"+str(minu))
