text = "Eggs #Bread #Butter #Milk"
print(text.split('#', 1))
print(text.split('#', 2))
print(text.split('#', 3))

text = "Thank you for the visiting\nWelcome to the web"
print(text.splitlines())
print(text.splitlines(True))
print(text.splitlines(False))

text = "two two is equal to five, five five is eight"
print(text.replace('five', 'four'))
print(text.replace('five', 'four', 2))

str = "Python is Easy and Powerfull"
print(str.partition('is '))
str = "Learn Python at Pydeep"
print(str.partition('is '))

# enumerate function
languages = [1, 'python', 2, 'c', 3, 'Java', 4, 'C#']
for item in enumerate(languages):
    print(item)
for item, value in enumerate(languages):
    print(item, value)
for count, item in enumerate(languages, start=10):
    print(count, item)

