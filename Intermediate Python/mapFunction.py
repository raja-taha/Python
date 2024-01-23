list1 = [1,2,3,4,5,6,7,8,9,10]

def function(x):
    return x**x

# print(list(map(function,list1)))

print([function(x) for x in list1 if x%2==0])