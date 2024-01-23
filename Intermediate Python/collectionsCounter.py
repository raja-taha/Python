from collections import Counter

c1 = Counter("Taha")
print(c1)
c2 = Counter(['a', 'a', 'b', 'c', 'c'])
print(c2)
c3 = Counter({'a':1, 'b':2})
print(c3)
c4 = Counter(cats=4, dogs=7)
print(c4)
print(c4['bird'])

print(list(c4.elements()))

print(c2.most_common(2))

c5 = Counter(a=4, b=2, c=0, d=2)
list1 = ['a', 'b', 'b', 'c', 'd']

c5.subtract(list1)
print(c5)

c5.update(list1)
print(c5)

c5.clear()
print(c5)
