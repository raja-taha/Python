# def function(x):
#     function2 = lambda x: x + 5
#     return function2(x) + 85
#
# print(function(2))
#
# function3 = lambda x, y: x + y
# print(function3(5, 5))

list1 = [1,2,3,4,5,6,7,8, 9, 10]

newList1 = list(map(lambda x: x+5, list1))
print(newList1)

newList2 = list(filter(lambda x: x%2==0, list1))
print(newList2)