
class A(Exception):
    pass

class B(A):
    pass
class C(B):
    pass

for cls in [A,B,C]:
    try:
        raise cls()
    except C:
        print(C)
        print('\t\tC')
    except B:
        print(B)
        print('\t\tB')
    except A:
        print(A)
        print('\t\tA')

for cls in [A,B,C]:
    try:
        raise cls()
    except A:
        print(A)
        print("\t\tA")
    except B:
        print(B)
        print('B')
    except C:
        print(C)
        print('C')

