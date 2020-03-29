# Opening the etc/hosts file and printing the contents of it to monitor output.
hosts = open('/etc/hosts')

hosts_file_contents = hosts.read()

print(hosts_file_contents)
print("That's it Boss for this file     " )

# # Opening the contents of the file examples.desktop from the home directory and posting the contest to output
# name_first_python_program = open('/home/jayakumar/examples.desktop')
# home_page_file_contents = name_first_python_program.read()
#
# print(home_page_file_contents)
#
# print("This is the end of file contents boss")

# validating the seek method of file function

print("current position of the file   {}".format(hosts.tell()))
print(hosts.read())

hosts.seek(180)
print("i am in the position of 180  ")
print("Printing from 180 the position to end of file {}")
print(hosts.read())
print(hosts.tell())
print("now printing nothing from the file as its already end position. lets get the position")
print("i am in the position of   ", hosts.tell())
print("now lets print it from the file as  nothing will print after this line")
print(hosts.read())

print("again am starting from 210th position of the file to the end of file ")
hosts.seek(210)
print(hosts.read())

print("now let us print from 0 position ")
hosts.seek(0)
print(hosts.read())

hosts.seek(20)
print("Find the now i have seek to 20 position ")

print("Is the file readable {}".format(hosts.readable()))
print(hosts.read(10))
print(" after reading 10 letters from file Now the position is ")
print(hosts.tell())


hosts.close()

