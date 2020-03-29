list_name = ['first','bear']

print(list_name)

# append , insert , extend (for whole lot)

list1 = ['cat','dog']
list2 = ['tiger','lion']

list3 = list1+list2
print("list concat {}".format(list3))

print("Before : List1 {} list2 {}".format(list1,list2))
list1.extend(list2)

print("After : List1 {} list2 {}".format(list1,list2))


index = 0
print(index)

while index < len(list_name):
    print(list_name[index])
    index = index+1


#printing elemnts in for loop

for name in list_name:
    print(name)


