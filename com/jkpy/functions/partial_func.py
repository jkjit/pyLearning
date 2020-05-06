from functools import partial


def simple_interest(p ,n ,r=0.1):
    print(f'Value of P:{p} \nValue of N:{n} \nValue of R:{r}')
    return ( p * n * r /100)

print(f"\nWhen 1000 and 3 are supplied: PNR value is {simple_interest(1000,3)}\n")

print(f'When all values 1000,3,0.5 are supplied PNR value is :{simple_interest(1000,3,0.5)}')

f= partial(simple_interest,1000)
print(f'When called function f with just two values 3,0.5 {f(3,0.5)}')

f1 = partial(simple_interest,1000,3)
print(f'When called function f1 with single value 0.5: {f1(0.5)}')
print("="*92)
print(f'f1 value {f1()}')
print("="*92)
f2 = partial(simple_interest,p = 1000, n= 3)
print(f'f2 value with blank: {f2()}')