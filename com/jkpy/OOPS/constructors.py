class A:

    def __init__(self):
        print("Am inside init of A class")

    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")


class B:
    def __init__(self):
        print("Am inside init of B class")

    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")


class C():

    def __init__(self):
        print("Am inside init of C class")

    def feature5(self):
        print("This is a feature 5")


class D(C,B):
    def __init__(self):
        super().__init__()
        print("Am inside init of D class")

    def feature6(self):
        print("Priting of featuer 6")


d1 = D()

d1.feature5()
d1.feature6()
