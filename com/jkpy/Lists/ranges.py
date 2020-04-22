

list_numbers = [1,2,3,4]
list_names = ['first','second','third']

list_animals = ['tiger','lion','cow']

for number in range(len(list_animals)):
    print(list_animals[number])

print("\n Printing the list_names : ")
print(list_names)
x= [value for value in list_names]
print("\nPrinting the value of x list here : \t")
print(x)

print("\nSlicing with increment : \n")
for number in range (1,3,1):
    print(list_animals[number])

print("\nSlicing with increment numbers : \n")

for number in range(1,3):
    print(number)
