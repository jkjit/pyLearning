# get input from user

class First:
    print(" Please enter any sentences or words : \t ")


# user_response = input()

# print("User has entered below \n " + user_response)
# create a dictionary to populate the values

# new_response = user_response.split()

# print(new_response)

value = "abc abc bcd bcd bcd jkjkjkl jkjk jkjkl jk jkjkl ssdd ssss ssssd ssssd"

words_list = value.split()

print(words_list)

second = {"word": 'value',
          "count": 0}

length = len(value)
print("length of the list is {} ".format(length))

# for i in len(value):

output = {'word': 0}
# while length <= 0:
#     length = -1
for i in range(0, len(value), 1):
        print("" + value[i])


def finder(some):
    output = {some[i]: some[i + 1] for i in range(0, len(some), 2)}
    return output


print(finder(value))

print(output)
#
# for value in range(len(new_response)):
#     print(" : ", value)
#
#         print("hello")

# print(new_response[0])

# while len(new_response)<=0

# while True:
#     counter = 0
#     response_value = {"word": counter}

# if input is blank exit the program

# if not blank extract words from the input

# Print individual word with word count
