class Car:

    wheels = 4

    def __init__(self,mileage,company):
        self.mileage = mileage
        self.company = company


car1 = Car(13,'BMW')
car2 = Car(12,'Jaguar')
car3 = Car("10", "Honda")

car1.wheels = 5

print("The car {} gives a mileage of {}".format(car1.company, car1.mileage))
print("The car {} gives a mileage of {}".format(car2.company, car2.mileage))

print("car1 wheels are {}".format(car1.wheels))
print("car2 wheels are {}".format(car2.wheels))


Car.wheels =3
# car1.wheels= Car.wheels


print("car1 wheels are {}".format(car1.wheels))
print("car2 wheels are {}".format(car2.wheels))
print("car3 wheels are {}".format(car3.wheels))

