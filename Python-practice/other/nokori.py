s = input().rstrip().split(" ")
m = float(s[0])
p = float(s[1])
q = float(s[2])

# print(m)
# print(p)
# print(q)

m = m*(0.01*(100-p))*(0.01*(100-q))
print(m)
