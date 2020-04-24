
list1 = ['cat', 'dog', 'lion', 'tiger','cat','lion']
list2 = ['pet','small','forestAnimal','fiery']
list3 = []
list1.extend(['SAMPLE'])
list1.extend(list2)

list1.append(list2)
list1.append('Elephant')
list3.append(list2)
print(list1)
print(list2)
print(list3)

print(list1.pop())
print(list1)

list1.insert(2,'New')
print(f'Inserted item in list1: {list1}')

print(list1.index('pet',0,len(list1)))
index = list1.index('pet',0,len(list1))
print(list1[index])
list2.remove('forestAnimal')
list4 = list2
list2.clear()
print(list2)

print('Total count of cats inside the list is:',list1.count('cat'),list1.count('lion'))

print(" {} {}".format(list1.count('cat'),list1.count('lion')))

print(f'{(list1.pop())}')