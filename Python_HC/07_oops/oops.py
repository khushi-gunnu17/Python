# Basic class and Object
# Create a car class with attributes like brand and model. Then create an instance of this class.
# self == this 


# class works like a blank form
from typing import Any


class Car :

    total_car = 0

    # constructor
    def __init__(self, brand, model) :     
        self.__brand = brand   # __ makes the attribute private, encapsulation
        self.__model = model
        # self.total_car
        Car.total_car += 1

    # setting a getter for brand attribute, can give any name besides get_ in the class name, but it's kind of breaking the convention, if given another name.
    def get_brand(self) :
        return self.__brand + "!"
    
    # def __setattr__(self, __name: str, __value: Any) -> None:
    #     pass


    def full_name(self) :
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self) :
        return "Petrol Or Diesel"
    
    # Decorators --> enhance the functionality of the methods
    @staticmethod       # objects cannot access this method, only class now
    def general_desc() :
        return "Cars are means of transport."
    
    @property      # can make the attribute read only and doesn't allow change , and can be accessed by the method only as an attribute
    def model(self) :
        return self.__model
    






# instance of the class
my_car = Car("Toyota", "Corolla") 
# my_car.model = "City"     # cannot do this now as property decorator is set and can be accessed now only as an attribute and not a function
# print(my_car.brand)       # cannot acces brand now, without a getter, as it is declared private in the Car class.
print(my_car.model)
print(my_car.full_name())
# print(my_car.general_desc())

# static method can only be accessed by the class and not the objects of the class
print(Car.general_desc())

print()


my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
print(my_new_car.model)







# inheritance
class ElectricCar(Car) :
    def __init__(self, brand, model, battery_size) :
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self) :
        return "Electric Charge"









print()
my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(my_tesla.model)
# print(my_tesla.brand)
print(my_tesla.get_brand())
print(my_tesla.full_name())
print(my_tesla.fuel_type())



print()









safari = Car("Tata", "Safari")
safariTwo = Car("Tata", "Nexon")
# can also create an object without giving a reference
Car("Suzuki", "Maruti")
print(safari.fuel_type())


print(Car.total_car)    # this is giving the reference of the nmber of times the construstor is called or the object of the class Car has been created.

print()









# Multiple Inheritance
class Battery :
    def battery_info(self) :
        return "This is battery"

class Engine :
    def engine_info(self) :
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car) :
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model X")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())