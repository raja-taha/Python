# s = {x for x in range(100)}
#
# print(98 in s) # O(1)
#
# s.add(101)
# s.remove(1)
# print(s.__len__())

s = {1, 2, 3, 7, 8, 'test'}
t = {3, 4, 5, 8, 9, 'test'}

print(s.intersection(t))
print(s.union(t))

ss = {1, 2, 3}
tt = {1, 2}
print(tt.issubset(ss))
print(ss.issubset(tt))
print(ss.issuperset(tt))
print(tt.issuperset(ss))

print(s.difference(t))
print(t.difference(s))

print(s.symmetric_difference(t))

h = s.copy()
h.remove(1)

print(h)
print(s)