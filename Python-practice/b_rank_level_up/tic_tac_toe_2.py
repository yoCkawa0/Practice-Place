# tmp = input()

# if tmp == "OOOOO":
#     print("O")
# elif tmp == "XXXXX":
#     print("X")
# else:
#     print('D')

board = input()
result = "D"

pivot = board[0]
count = 0
for stone in board:
    if stone != "." and stone == pivot:
        count += 1
    else:
        break

if count == 5:
    result = pivot

print(result)
