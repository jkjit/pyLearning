

user = {
    'Name': "John",
    'Age': 30,
    'Email': 'john@email.com'
}

print(" Iterating all user items inside a Dictionary ")
for items in user.items():
    print(items)

print("\nIterating all user items inside a using only Keys at first level ")
for items in user:
    print(items)

print("\nIterating all user items inside using only Keys at first and second levels ")
for keys in user:
    # print("{},{},{}".format(keys[],keys[1],keys[2]))
    # print("{},{},{}".format(user['Name'],user['Age'],user['Email']))
    print(" {} : {}".format(keys,user[keys]))

print("\n only the keys with center aligned ")
for items in user.keys():
    print(items.center(30))
