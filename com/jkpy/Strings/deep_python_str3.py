import math

#zip function

num = [1,2,3,4,5,6]
languages = ['python', 'c++', 'c#', 'java', 'cobol', 'swift']

result = zip(num,languages)

print(list(result))
langList = [(1, 'python'), (2, 'c++'), (3, 'c#'), (4, 'java'), (5, 'cobol'), (6, 'swift')]
index, lang = zip(*langList)
print(f'index :{index} and languages: {lang}')

#map function map(function_name, iterable)

def factorial_list(n):
    return math.factorial(n)
numbers = [1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10]

factorial_result = map(factorial_list,numbers)
print(factorial_result)
print(list(factorial_result))

#sorted function.

sorted_List = ['a', 'u', 'e', 'i', 'o']
print(sorted(sorted_List))
print(sorted(sorted_List,reverse=True))