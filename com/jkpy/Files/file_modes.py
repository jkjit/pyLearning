
file_path = "/home/jayakumar/test1"

"""with open(file_path) as fpath:
    print(fpath.read())

with open(file_path,'a') as fpath:
    print("is this file writeable :{} \t".format(fpath.writable()))
    fpath.write("This text get added to the end of file")
    # print(fpath.read())

with open(file_path,'a') as fpath:
    fpath.write("GRAND one")
    print("Is this file readable: {} \t".format(fpath.readable()))

with open(file_path,'r') as fpath:
    print(fpath.read())"""

with open(file_path+"3",'r+') as file:
    file.read()
    file.write("Something written with w")
    file.seek(0)
    print(file.read())
