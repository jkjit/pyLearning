class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Am inside the class  with computer details CPU: {} and Ram: {}\n".format(self.cpu, self.ram))


com1 = Computer('Intel5',4)

com1.config()
