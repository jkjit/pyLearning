print("Starting the read of the file. ")
with open('/etc/hosts') as hosts:
    print("Is the file Closed? {} ".format(hosts.closed))
    print(hosts.read())

print("Finished reading the file ")
print("Is the file now closed as we didnt specify the file close command. is closed {}".format(hosts.closed))


print("Again using iteration method as for loop and getting contents line by line ")

with open('/etc/hosts') as filename:
    for line in filename:
        print(line)

print("Done with for loop for the file")

# code for stripping white spaces using strip method
with open('/etc/hosts') as hosts:
    for line in hosts:
        print(line.strip())
print("End of using strip method")
# code for stripping white spaces with rstrip method
with open('/etc/hosts') as hosts:
    for line in hosts:
        print(line.rstrip())

print("End of using rstrip method")