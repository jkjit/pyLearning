
str = "abc@gmail.com"

print("Position of com inside an email is")
print(str.find('com'))

print(str.isalnum() ,str.isalpha() ,str.isdecimal() ,str.isdigit() ,str.islower() ,str.isprintable() ,str.istitle())
print("* " *82)
print(str.replace('@gmail' ,'@hotmail'))

print(str)
print(str.replace('@' ,'@hot'))

print(str.endswith('.com'))
print(str[:-4:])
str1 = "bigemailaddrress@gmail.com"
str2 =""
for i in str1:
    if i != '@':
        str2+=i
    else: break
print(str2)
print("Using While loop")
str2 =""
for i in range(len(str1)):
    if str1[i] != '@':
        str2 +=str1[i]
    else: break
print(str2)

str = "Example"

print(str.__len__())
print(len(str))

length = ((str).join(str)).count(str)+1
print(length)

# print((str).join(str))

counter = 0
for i in str:
    counter+=1

print("using for loop the Length is",counter)

counter=0
while str[counter:]:
    counter+=1
print("Using while loop the length is ", counter)


str = "TutorialsPoinz"

position = 0
while str[position:]:
    position +=1
print("Length is ",position)

print(str[::])
print(str[0:len(str)])
print(str[-1:])
print(str[::-1])
print(str[-3::-1])
print(str[-3::1])
print(str[-3:])
print(str[-3:-1])
print(str[:1])
print(str[:-1])
print(str[-3:-4:-1])
print(str[-3:-2:1])

print(str[:3:-1])
print(str[:3])
print(str[:9:-1])
print("===========")
print(str[-12:-15:-1])
#
# def extendlist(val,list=[]):
#     list.append(val)
#     return list
#
# list1 = extendlist(10)
# print(list1)
# list2=extendlist(20,[])
# print(list2)
# list3=extendlist('a')
# # print(list1,list2,list3)
# print(list1)
# print(list2)
#
