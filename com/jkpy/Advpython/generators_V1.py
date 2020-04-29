import sys
import time
# Normal function
def getList(limit):
    listVal = list()
    for i in range(limit):
        listVal.append(i)
    return listVal
# Generator function
def genList(limit):
    for i in range(limit):
        yield i

if __name__ == '__main__':
    numLimit = 10000000
    print("\n Without Generators:" )
    startTime = time.time()
    numList = getList(numLimit)
    endTime = time.time()
    print("Time diff is : ",endTime-startTime)
    print(sys.getsizeof(numList))

    print('\n with generators')
    startTime = time.time()
    numGenerator = genList(numLimit)
    endTime = time.time()
    print("Time diff is : ", endTime - startTime)
    print(sys.getsizeof(numGenerator))