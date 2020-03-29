from time import asctime, sleep

import time

import sys
# print(sys.path.sort())

print("LEts print the path")

print("here is the count", (sys.path.count(2)))

print(sys.path)

print("again printing using for loop")

for path in sys.path:
    print(path)
print(asctime())
sleep(1)
print(asctime())

print("This is the tme method", time.time())
print ("THis is the ", time.clock())

print(time.ctime(3))

print(dir(time))

print("the computer cpu time is", time.CLOCK_PROCESS_CPUTIME_ID)