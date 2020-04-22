class Student:

    def __init__(self, name_input, roll_input, laptop_input):
        self.name = name_input
        self.roll = roll_input
        self.lap = laptop_input

    def show(self):
        print(self.name, self.roll, self.lap.brand, self.lap.cpu, self.lap.ram)

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram


hp_latop = Student.Laptop("HP", 8, 2)
dell_laptop = Student.Laptop("Dell", 20, 4)

s1 = Student("Rama", 1, hp_latop)

s1.show()

# print("student Laptop brand is ", s1.lap.brand)
s2 = Student("Krishna", 2, dell_laptop)
s2.show()
