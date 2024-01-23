from collections import deque

# d = deque("hello", maxlen=5)
d = deque("hello")

d.append("4")
d.append(5)
d.appendleft(5)
print(d)

d.pop()
d.popleft()
print(d)

# d.clear()
# print(d)

d.extend('456')
d.extend('hello')
d.extendleft('hello')
print(d)

d.rotate(-1)
print(d)