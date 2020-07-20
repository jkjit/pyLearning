print("*"*120)
print("SWAPPING".center(80," "))
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)
print("*"*120)

print("Combining List of strings into single One".center(80," "))
sentence_list = ["my", "name", "is", "George"]
print(f'Before: {sentence_list}')
sentence_string = " ".join(sentence_list)
print(f'After : {sentence_string}')
print("*"*120)

print("Splitting strings into list of Substrings".center(80," "))
split_sentence_string = "my name is George"
print(f'Before: {split_sentence_string}')
print(f'After:  {split_sentence_string.split()}')
print("*"*120)

print("Initialising a list filled with some number".center(80," "))
[0]*1000 # List of 1000 zeros
[8.2]*1000 # List of 1000 8.2's
print(f'List of 0 100 times : {[0]*100}')
print(f'List of 8.2s 200 times : {[8.1]*200}')

print("*"*120)
print("Merging dictionaries".center(80," "))
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x,**y}

print(x,y,z, sep="\n")

print("*"*120)
print("Reversing a String".center(80," "))
str1 = "SIMPLE"
print(f'Before: {str1}, and After: {str1[::-1]}')

print("*"*120)
print("Returning multiple values from a function".center(80," "))

def get_multi_values():
    a = "Google"
    b = "is"
    c = "Cool"
    return a,b,c
print(f'Printing function by using directly : {get_multi_values()}')
first, second, third = get_multi_values()
print(f'Assigning values as well: We get first:{first}, Second : {second}, Third: {third}')

print("*"*120)
print("List comprehension".center(80," "))
list1 = [1,2,3,4]
list2 = [num*2 for num in list1]
print(f'FirstList: {list1}, Second List after multiplying each: {list2}')

print("*"*120)
print("Iterating over a Dictionary".center(80," "))
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f'Dictionary :{m}')
for key,item in m.items():
    print(f'Key:{key}, Value:{item}')

print("*"*120)
print("Iterating over list values while getting the index too".center(80," "))
m = ['a', 'b', 'c', 'd']
print(f'Printing list: {m}')
for a, b in enumerate(m):
    print(f'Index: {a}, Value: {b}')

print("*"*120)
print("Initialising empty containers".center(80," "))

a_list = list()
a_dict = dict()
a_set = set()
print(f'This is list:{a_list}, This is blank dict:{a_dict}, This is a blank Set: {a_set}')

print("*"*120)
print("Removing useless characters on the end of your string".center(80," "))
name = "   Google "
name_1 = "Google////"
print(f'First string before: {name}, Second String Before: {name_1}')
print(f'first string after: {name.strip()}, Second String After :{name_1.strip("/")} ')

print("*"*120)
print("Find the most frequent element in a list".center(80," "))
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test),key=test.count))

print("*"*120)
print("Check the memory usage of an object".center(80," "))
import sys
x = 4
print(f'Memory of integer x is : {sys.getsizeof(x)}')

print("*"*120)
print("Convert a dict to XML".center(80," "))
from xml.etree.ElementTree import  Element

def dict_to_xml(tag,d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

a_var =10
print("a_Var is at: ", dir())

def b():
    b_var = 11
    print("Bvar_var is at : \t", dir())
b()

print("end is at : ", dir())




