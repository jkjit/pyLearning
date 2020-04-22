list_name = ['first', 'bear']

print(list_name)

# append , insert , extend (for whole lot)

list1 = ['cat', 'dog']
list2 = ['tiger', 'lion']
list3 = list1 + list2
print("list concat with + symbol \t:{}".format(list3))

print("Before : List1 {} \t\tlist2 {}".format(list1, list2))
list1.extend(list2)

print("After : List1 {}\t\t list2 {}".format(list1, list2))
print(list3)
list1.reverse()

print("==== reversed it===========")
print(list1)

list1.reverse()
print("==== reversed it AGAIN===========")

print(list1)
# printing elements in for loop

list1.sort()
print("===== Sorted =====")
print(list1)

for name in list_name:
    print(name)

print(list_name)
