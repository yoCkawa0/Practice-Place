# n = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
# sum = 0
# for i in range(len(n)):
#     q = n.count(n[i])
#     if sum < q:
#         sum = q
# print(sum)

array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
count = {}

for pattern in array:
    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1

for (key, value) in count.items():
    if value != 1:
        print(value)
