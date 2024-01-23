def add7(x):
    return x + 7

def isOdd(x):
    return x % 2 != 0

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list(filter(isOdd, list1))

list3 = list(map(add7, filter(isOdd, list1)))

print(list1)
print(list2)
print(list3)