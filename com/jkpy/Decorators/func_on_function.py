def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    return func(x)


print("\n\n\n\nIncrement of 3 is {} ".format(operate(inc, 3)))

print("\nDecrement of 5 is : {} \n".format(operate(dec, 5)))


def is_called():
    def is_returned():
        print("Hello \n")

    return is_returned

# way of calling the function . as it is returning the function we need to add () so that it acts as a function
is_called()()

# Another way of calling is by assigning some variable . here we used caller. which becomes a function at the
# assignment as it has to catch a function
caller = is_called()

# Outputs "Hello"
caller()
