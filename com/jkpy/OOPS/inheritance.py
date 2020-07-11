class A:

    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")


class B:
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

class C(A):
    def feature5(self):
        print("This is a feature 5")

class D(B,C):
    def feature6(self):
        print("Printing of feature 6")
    def feature5(self):
        print("Printed modified logic from D for feature 5")


d1 = D()

d1.feature1()
d1.feature5()
d1.feature6()