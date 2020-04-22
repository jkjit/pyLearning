input_map = {}


def process_user_input(input_value):
    input_list = input_value.split()
    if len(input_list) != 2:
        print("Invalid input")
    else:
        print("Valid input.. Good")
        input_map[input_list[0]] = input_list[1]


proceed = True

while proceed:
    print("Current input MAP we have ")
    print(input_map)
    user_input = input("Give me 2 words. Press Enter to Exit: ")
    if len(user_input) == 0:
        proceed = False
        print("Exiting now.. here is the final MAP")
        print(input_map)
    else:
        print("You entered {}".format(user_input))
        process_user_input(user_input)
