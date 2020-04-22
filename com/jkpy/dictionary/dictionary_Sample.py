# my_dict = dict({1:'apple', 2:'ball'})
# print(my_dict)
# print(type(my_dict))
#
# my_dict1 = dict([(1,'apple'), (2,'ball')])
# print(my_dict1)
# print(type(my_dict1))

my_dict = {'name': 'jack', 'age': 20}

print(my_dict)

print(my_dict['name'])
print(my_dict.get('name'))
print(my_dict.get('age'))

squares = {1:1, 2:4, 3:9, 4:16, 5:25}

print(squares)
print(squares.pop(3))
print(squares)
print(squares.popitem())
print(squares.popitem())
print(squares)
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)
print((squares.items()))
print(squares.keys())
print(squares.values())
print(squares)
print(squares.popitem())
print(squares)
squares.__delitem__(2)
print(squares)
squares.clear()
print(squares)
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)
squares.__dir__()
# print(squares.__dir__())

print(squares.__getitem__(1))
squares.__setitem__(1,20)
print(squares)

if squares.__contains__(6):
    print("dictionary contains the value specified")
else: print("Doesnt have this key")

squares.setdefault(1)
print(squares.__len__())

print(len(squares))

str2 = squares.copy()
print(str2)

print("Salary not found: "+ str2.get('salary','UselessFellow'.upper()))
print(str2)