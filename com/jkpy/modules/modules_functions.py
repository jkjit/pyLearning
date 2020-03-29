def say_hi():
    print("ITs just saying hi when some one calls this method say_hi ")


def main():
    print("Hello from main method")
    say_hi()
    text = input ('what you want your cat look like')
    cat_say(text)

def cat_say(text):
    # Here the code does the job of printing the cat image
    text_len = len(text)

    print('        {}'.format('_'*text_len))
    print('      < {} >'.format(text))



if __name__ == '__main__':
    main()

