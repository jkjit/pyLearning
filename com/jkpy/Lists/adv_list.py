import copy

list1 = [1,[2,3],4]
list2 = ['a',['b','c'],'d']
print(f'printing both new lists\n list1: {list1} and list2: {list2}')

list3 = copy.copy(list1)
list4 = copy.deepcopy(list2)

print(f'before modifying lists shallow \n list1: {list1} list3: {list3}')
list3[0]=9
list3[1][0] = 800
print(f'shallow copy reflecting after changes \n list1:{list1} and list3:{list3}')
print(f'*'*82)

print(f'Before modifying deep copy \n list2:{list2} and list4:{list4}'.rjust(120,"+"))
list4[1][0]='Ball'
print(f'After deep copy changes \n list2:{list2} and list4:{list4}'.rjust(120,"+"))

#
# list1 = [1,2,3]
# list2 = ['a','b','c']
#
# list3 = copy.copy(list1)
# print(f'Before modifications shallow copy \nlist1:{list1}, list3:{list3}')
# list4 = copy.deepcopy(list2)
# print(f'Before modifications deep copy\nlist2:{list2}, list4:{list4}')
#
# list3[0]=14
# print(f'After modifying list3 \n list3: {list3}, list1: {list1}')
#
# list4[0]='apple'
# print(f'After modifying list4 \n list4: {list4}, list2:{list2}')

# basic_list1 = [1,2,3]

# basic_list2 = [5,4,6]
#
# two_level_list = [basic_list1, basic_list2]
#
# shallow_copy_list_1 = copy.copy(two_level_list)
# deep_copy_1 = copy.deepcopy(two_level_list)
#
# print(two_level_list)
# print(shallow_copy_list_1)
# print(deep_copy_1)
#
# two_level_list[0][0]=10
# print(two_level_list)
# print(shallow_copy_list_1)
# print(deep_copy_1)
