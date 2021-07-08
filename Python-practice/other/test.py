s = input().rstrip().rsplit()
a = int(s[0])
b = int(s[1])
c = int(s[2])
n = int(input())
m = [input().split() for l in range(n)]
# dead = 539
d = 539 - c - b
paiza = 0
paizamax = 0
# deadi = 0
for i in range(n):
    # hour = int(s[i][0])
    # minu = int(s[i][1])
    deadi = ((int(m[n-i-1][0]) * 60) + int(m[n-i-1][1]))
    print(deadi)
    if deadi <= d:
        paiza = deadi
        if paizamax <= paiza:
            paizamax = paiza
t = paizamax - a
hour1 = int(t//60)
minu1 = t - (hour1*60)
print("0"+str(hour1)+":"+str(minu1))

# if hour1 > 9:
#     print(str(hour1)+":"+str(minu1))
# else:
#     print("0"+str(hour1)+":"+str(minu1))
