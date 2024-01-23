from collections import namedtuple

# point = namedtuple('Point', ['x', 'y', 'z'])
point = namedtuple('Point', 'x y z')

newP = point(3, 4, 5)
print(newP)

print(newP.x, newP.y, newP.z)
print(newP._asdict())
print(newP._fields)
print(newP._replace(y=6))

p2 = point._make(['a', 'b', 'c'])
print(p2)
