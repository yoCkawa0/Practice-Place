result = "D"
for i in range(5):
    c = 0
    tmp = input()
    cri = tmp[0]

    for stone in tmp:
        if stone != "." and stone == cri:
            c += 1
        else:
            break
    if c == 5:
        result = cri

print(result)
