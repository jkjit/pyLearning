

# del statement to delete the item


contacts = {'jack':'1234', 'daniel':'5678'}
print("Before adding new contacts : {} ".format(contacts))

contacts['rob'] = '3456'
print("Adding rob number to contacts: ")
print(contacts)

contacts['bob'] = ['123456', '98765','2e13123']


for name in contacts:
    print("Name of the person: " +name)
    print("phone number is {} ".format(contacts[name]))


"""print("removing jack from contacts list : ")

del contacts['jack']
print(contacts)"""