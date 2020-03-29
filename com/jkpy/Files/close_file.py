hosts = open('/etc/hosts')

hosts_file_contents = hosts.read()

print(hosts_file_contents)
print("That's it Boss for this file     " )

hosts.flush()
hosts.close()

if not hosts.closed:
    hosts.close()
print("The file is closed")

print("now again open the File and check if condition \n\r\n ")
hosts = open('/etc/hosts')

# if not hosts.read():

if not hosts.closed:
    print(hosts.read())

hosts.close()