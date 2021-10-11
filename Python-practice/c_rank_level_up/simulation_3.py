h = int(input())

h -= 2
p = 1
p1 = 1
p2 = 0
m = 1
m1 = 1
m2 = 0
c = 2

while h > 0:
    p2 = p1
    m2 = m1
    p1 = p
    m1 = m

    p = (m1+m2)
    m = ((p1*2)+p2)
    h -= m
    c += 1

print(c)
