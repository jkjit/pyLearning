class Computer:

    def __init__(self):
        self.cpu = 'Intel'
        self.ram = 8

    def config(self):
        print("Am inside the class  with computer details CPU: {} and Ram: {}\n".format(self.cpu, self.ram))

    def compare_config(self, other):
        if self.cpu == other.cpu and self.ram == other.ram:
            print("Both configurations are Same")
            return True
        else:
            print("Both configurations are different")
            return False


com1 = Computer()
com2 = Computer()

com1.ram =4

print(com1.compare_config(com2))
