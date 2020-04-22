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

words_map = {}

for word in words_list:
    if word in words_map.keys():
        current_count = words_map[word]
        current_count = current_count+1
        words_map[word] = current_count
    else:
        words_map[word] = 1

print(words_map)