# d = {'apple':4, 'banana':2, 'cherry':6}
# print(d['apple'])
#
# d[(2, 3)] = 7
#
# # d.clear()
#
# print(d)

s = 'hellomynameis'

counts = {}

for char in s:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)

for key in counts:
    print(key)

for i in counts.values():
    print(i)

for key, i in counts.items():
    print(key, i)