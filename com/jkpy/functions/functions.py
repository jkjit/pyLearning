from com.jkpy.Strings.strings import say_hifi


def greet(name='there', age=2000, email="foo.com"):
    """Intoduce the employee"""
    print("Hey {}, You are {} years old and your email is {}".format(name, age, email))

"""
help(greet)
greet("mahesh", 34, "pmahesh@cisco.com")
greet()
greet(email='jk.com', age=36)

greet(email='jk.com', age=36, name="JK")
"""

greet(email="p@ga.com",age=20, name="pa")

def get_input_and_greet():
    name = input("Enter your name: ")
    age = int(input('ENter you age: '))
    email = input("Enter your email: ")
    greet(name,age,email)
    print(say_hifi(name))


get_input_and_greet()
