from itertools import zip_longest

list1 = list(range(10))
list2 = list(range(10,25))
print(list1,list2)

print(list(zip(list1,list2)))
print(list(zip_longest(list1,list2,fillvalue="none")))
long_zip = list(zip_longest(list1,list2,fillvalue="none"))
print(long_zip)

a,b = zip_longest(*long_zip)
print(a)
print(b)