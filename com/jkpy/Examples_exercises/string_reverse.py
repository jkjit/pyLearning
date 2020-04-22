

first_str = "hello WORLD"

for index in range(0,len(first_str),1):
    print(str(index)+"   "+first_str[index])

print("===============with only two arguments=============")
for index in range(0,len(first_str)):
    print(first_str[index])

print("===============REVERSE=============")
for index in range(len(first_str)-1, -1, -1):
    print(str(index) + "   " + first_str[index])

print("===============Using build in method==========")

print(first_str.swapcase())
print(first_str.lower())


print(first_str.split('*'))