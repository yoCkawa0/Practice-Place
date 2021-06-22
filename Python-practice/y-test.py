import sys

n = int(input())
a = [0]*n

b = input().rstrip().split(" ")
for i in range(n):
    a[i] = int(b[i])
a.sort()
max = a[-1]
min = a[0]

print(min, max)
for i in range(n):
    print(a[i], end="")

#


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


# １問目
i = input().split()
n = int(i[0])
k = int(i[1])
sum = 0

print(n)
print(k)
for i in range(n):
    a = input().split()
    b = int(a[0])
    c = int(a[1])
    if b >= k:
        sum += c
print(sum)
