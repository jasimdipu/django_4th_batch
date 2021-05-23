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
        print(i*10)
    else:
        print(i, " is an string value")
