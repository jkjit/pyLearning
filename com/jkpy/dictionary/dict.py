
root = { x**2 for x in range (1 ,15 ,1)}
print(root)

print(sorted(root))
root = { x**2 for x in range (15 ,1 ,-1)}
print(root)

root = { x**2 for x in range(0 ,5 ,-1)}
print(root)

root = { x**2 for x in range(5 ,0 ,1)}
print(root)

print(type(root))

newval = {x**2 for x in range(1,8)}
print(newval)

# l1 = [1 ,4 ,3]
# print(l1)
# print(l1[::-1])

#
# print(1.1 +2.2 >3.3)
#
# print( True>=False )
#
# print( 7/2)
# print( 7//2)
#
#
# str1 = "Appointment"
# print(str1.title())
# print(str1.format())
# print((str1.count(str1)))
# print(str1.split('me'))
#
# # print(str1.index('m','e'))
# def me():
#     """
#     This function returns if str1 "Appointment" contains 'me' in it else it prints else block statement
#     :return:
#     """
#     if 'me' in str1:
#         return ("me found in "+str1)
#     else:
#         return "Nothing found in that string"
# print(me())
#
# print(me.__name__)
# print(me.__code__)
# print(me.__doc__)
# print(me.__dict__)
# print(me.__closure__)
# print(me.__annotations__)
# print(me.__globals__)
# print(me.__qualname__)
# print(me.__module__)
# print(me.__sizeof__())