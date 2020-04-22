class Student:
    """ This is a Class variable and doesnt change for each student"""
    school = "S.V.High School"

    def __init__(self, m1, m2, m3,name):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.name = name

    def avg(self):
        """ This is a instance method since it uses self"""
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_school_name(cls):
        return cls.school

    @staticmethod
    def any_method():
        print("This is a just static method neither use class nor instance variables")

    @staticmethod
    def plus_1(input_value):
        return input_value+1

    def minus_1(self, input_value):
        return input_value-1


s1 = Student(12, 14, 44 , 'Rama')
s2 = Student(15, 14, 67, 'Krishna')
s3 = Student(56, 76, 98, 'Govinda')

student_list = [s1,s2,s3]

for stud in student_list:
    print("Student {} has an average of  {}".format(stud.name,stud.avg()))

print(" ALl studetns belong to {}".format(Student.get_school_name()))

Student.any_method()

print("Calling the static method with value 20 and it returns :  \t", Student.plus_1(20))


print("Printing a minus method to print values of 20 it returns: \t", s1.minus_1(20))