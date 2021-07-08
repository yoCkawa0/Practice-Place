#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hello world")


# In[4]:


input_line = input()
s = input_line.rstrip().split(' ')
a = int(s[0])
b = int(s[1])
print(a + b)


# In[5]:


a = 0
low = 160
for i in range(5):
    a = int(input())
    if low >= a:
        low = a
print(low)


# In[6]:


input_line1 = input()
input_line2 = input()

if input_line1 == input_line2:
    print("OK")
if input_line1 != input_line2:
    print("NG")


# In[ ]:


g = int(input())

for i in range(g):
    j = i + 1
    if j % 3 == 0 and j % 5 == 0:
        print("FizzBuzz")
    elif j % 5 == 0:
        print("Buzz")
    elif j % 3 == 0:
        print("Fizz")
    else:
        print(j)


# In[ ]:


g = int(input())

for i in range(g):
    j = i + 1
    if j % 3 == 0 and j % 5 == 0:
        print("FizzBuzz")
    elif j % 5 == 0:
        print("Buzz")
    elif j % 3 == 0:
        print("Fizz")
    else:
        print(j)


# In[ ]:


# プログラムカウンター
l = 0

# 入力を格納
input_line = input()
# スペースで分けてsに格納
s = input_line.rstrip().split(' ')

# n 座先数
n = int(s[0])
# m グループ数
m = int(s[1])

for i in s:
    

print(n)
print(m)

# 着席できたグループ数
print(l)


# In[ ]:


# プログラムカウンター
l = 0

# 入力を格納
input_line = input()
# スペースで分けてsに格納
s = input_line.rstrip().split(' ')

# n 座先数
n = int(s[0])
# m グループ数
m = int(s[1])

# s[2]からs[]
for i in range(m):
    print(i)

print(n)
print(m)

# 着席できたグループ数
print(l)


# In[ ]:




