class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Am inside the class  with computer details CPU: {} and Ram: {}\n".format(self.cpu, self.ram))

    def compare_config(self, other):
        if self.cpu == other.cpu and self.ram == other.ram:
            print("Both configurations are Same")
            return True
        else:
            print("Both configurations are different")
            return False


com1 = Computer('Intel5', 4)
com2 = Computer("Intel5", 5)

print(com1.compare_config(com2))
