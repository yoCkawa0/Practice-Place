n = int(input())
list = []
for i in range(n):
    a = input()
    if a in list:
        list.remove(a)
        list.insert(0, a)
    else:
        list.insert(0, a)

print("")
for i in list:
    print(i)
