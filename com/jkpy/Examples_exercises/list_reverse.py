list1 = [1, 2, 3, 4]

print(list1)

print("Reversed list is \n")

print(list1[::-1])
print(list1[::2])

dictionary = {"Kadugudi": 560067,
              "whiteField": 56000,
              "Marathhalli": 555500
              }
print("========================================")

for area in dictionary:
    print("Area name: {} and its pin code: {}".format(area, dictionary[area]))

print("========================================")

for area in dictionary.keys():
    print("Area name: {} and its pin code: {}".format(area, dictionary[area]))

dictionary["jp nagar"] = 560067
print("========================================")
for area, pin in dictionary.items():
    print("Area name: {} and its pin code: {}".format(area, pin))

print("========================================")
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

print("========================================")
for pin in dictionary.values():
    print("Area name: NOTSURE and its pin code: {}".format(pin))


for area, pin in dictionary.items():
    if pin%10 == 7:
        print(area,pin)


# 4567 = 567
# 123 = 23
# 1234567 = 234567
#

# input = 4567
# print(str(input)[1::])

inpu = 647484
devide_by = 10 ** (len(str(inpu))-1)
print(inpu)
print(devide_by)
print(inpu%devide_by)
input_str = str(inpu)
print(input_str[:len(input_str)-1:])