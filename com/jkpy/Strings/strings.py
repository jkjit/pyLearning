

def say_hifi(name):
    return 'Hifi ' + name

def try_outs():
    print("hello {}")

    print("hello {} and {}, how are you!!!".format('jk', 'ck'))

    intvalue = 3
    print('hello ' + str(intvalue))
    print('hello {}'.format(intvalue))

    furits_list = [1, 2, 'apple']

    print("Hello in this list" + "{}" + "{} {} {}".format(furits_list[0], furits_list[1], furits_list[2]))
    print("we areusing lists inside lists {}".format(furits_list))


    print('hello {0} {0} {0:^20}, how are you? '.format('jk'))

    print("HI {0} {0} {0}".format(furits_list[0]))



    """
    greet_message = "Welcome you have entered {} value"
    # user_input = input("Enter a value")
    
    # print(greet_message.format(user_input))
    print("Welcome you have entered a {} value".format(input("Please enter your name")))
    
    Slicing Example"""
    fruit = 'Apple'
    print(fruit)
    print(fruit[:3:])  # App

def sting_slicing():
    animal = 'horse'
    name = 'acede@gmail.com'
    # print(animal[1:3:2])
    print("Index of @ : {} ".format(name.find('@')))
    print(name[:name.find('@')])
    # print(name)
    # print(name[:-10])

sting_slicing()
