class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):2
        return self.__brand + "!"

    def full_name(self):
        return f"{self.model} {self.__brand}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod
    def description(): 
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla =  ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.get_brand())
print(my_tesla.get_brand())
print(my_tesla.full_name())   
print(my_tesla.fuel_type())

print(Car.total_car)

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
print(my_new_car.fuel_type())