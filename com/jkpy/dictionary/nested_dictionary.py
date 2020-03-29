

contacts = {
    'Rob': {
        'phone': '242412412',
        'email': 'rob@email.com'
    },
    'jason': {
        'phone' : '121412412',
        'email': 'abc@email.com'
    },
    'maddy': {
        'phone': '34521412412',
        'email': 'maddy@email.com'
    },
    'bob': {
        'phone': '6567412412',
        'email': 'bob@email.com'
    }
}

print(contacts)

for contact_name in contacts:
    contact_info = contacts[contact_name]
    print(contact_name+" "+contact_info['phone']+" "+contact_info['email'])

#
# for key in contacts:
#     print(" Name : {} , Phone : {}, Email : {}".format(key,contacts[key]['phone'],contacts[key]['email']))