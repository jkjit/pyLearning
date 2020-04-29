greeting = "this is the greeting"

print(greeting)
print("Length of the greeting is "+ str(len(greeting)))

#printing the upper case letters
print(greeting.upper())

print(greeting)
print("This is lower case\n"+ greeting.lower())

# print(greeting.swapcase())
print(greeting.startswith('is'))
print(greeting.startswith('this'))
print(greeting.endswith('greeting'))

print(greeting.strip('This'))
print(greeting.strip('is'))
print(greeting.strip('is the'))
print(greeting.strip('greeting'))
