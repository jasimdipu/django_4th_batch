# list, tuple, set, dictionary

l = [1, 2, 3, 4.5, 6.5, 7.5, "Seven", "eight", 'nine']
print(type(l))
print(l)

# indexing
print(l[6])
print(l[0])
print(l[-2])

# slicing
print(l[1:7])
print(l[4:])
print(l[:5])
print(l[::-1])

# mutable and immutable

l[0] = 100
print(l)

t = (10, 20, 30)
print(t)
# t[0] = 1000

for i in l:
    if type(i) == int or type(i) == float:
        print(i * 10)
    else:
        print(i, " is an string value")

new_list = [92, 34, 63, 74, 28, 31, 50, 26]
print("before sorting", new_list)
new_list.sort()
print("After sorting", new_list)

print(new_list.pop())

print(new_list)

print(new_list.pop(0))

print(new_list)

lst = [2, 34, 34, 12, 6, 6, 6, 3, 54, 3, 6, 7]

print(lst.count(6))

print(lst.index(34))
lst.append(50)
print(lst)
lst.insert(1, 20)
print(lst)
lst.remove(34)
print(lst)

lst.reverse()
print(lst)

# nested list
import numpy as np

nes_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nes_list[1][1])
print(np.ndim(nes_list))
arr = np.array(nes_list)
print(arr)
print(np.ndim(arr))
# list comprehension
print(type(l))
for i in l:
    print(i)
    print(type(i))
print("List Comprehension")
print([i for i in l])
print([i for i in range(10) if i % 2 == 1])
var = [i for i in range(10) if i % 2 == 0]
print(var)

