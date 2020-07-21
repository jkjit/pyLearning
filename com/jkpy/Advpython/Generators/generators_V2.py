
import sys

def custom_chain(*something):
    for i in something:
        yield from i

print(sys.getsizeof(custom_chain()))
for x in custom_chain([1,2,3,4,5,6,7,8,9],'Soemthing big string'):
    print(x, end=' ')

print('\n',sys.getsizeof(custom_chain()))