import time
import sys

#Normal function
def normal(num):
    listval = list()
    for i in range(num):
        listval.append(i)
    return listval
def list_comprehension(numlist):
    listva11 = list()
    for i in numlist:
        listva11.append(i)
    return listva11
def gen(num):
    for i in num:
        yield i

if __name__ == '__main__':
    num = 10000000
    print("With range function: ")
    start = time.time()
    numlist = normal(num)
    print(type(numlist))
    end = time.time()
    print(f'Diff is : {end-start}')
    print(f'The size of memory taken by this normal function is  : {sys.getsizeof(numlist)}')
    print("="*92)

    print("With List comprehension:")
    start = time.time()
    comlist = list_comprehension(numlist)
    print(type(comlist))
    end = time.time()
    print(f'Diff timeis : {end-start}')
    print(f'Memory size is: {sys.getsizeof(comlist)}')
    print("="*92)

    print("with Generators")
    start = time.time()
    genlist = gen(num)
    print(type(genlist))
    end = time.time()
    print(f'Diff in time is : {end-start}')
    print(f'The size of memory taken by generator is : {sys.getsizeof(genlist)}')
