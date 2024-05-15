
class Car:
    # ! Class Attribute
    # Belongs to the class car
    cars = []
    year = None

    def __init__(self, color , hp , model):
        # ! Instance Attributes
        # Belongs to individual objects
        self.color = color
        self.hp = hp
        self.model = model

        Car.cars.append(self)
    
    # ! Instance Methods
    def display_info(self):
        print(f"Color => {self.color}")
        print(f"HP => {self.hp}")
        print(f"Model => {self.model}")

    # ! Class Methods
    @classmethod
    def display_car_count(cls):
        print(f"Total number of cars: {len(cls.cars)}")

    @classmethod
    def display_year(cls):
        print(f"Year = {cls.year}")

    @staticmethod
    def calculate_mileage(gaz_capacity , hp):
        print(f"The current gaz will take you {(gaz_capacity / hp) * 120} Miles")

Car.year = 2002
car_1 = Car("Red" , 60 , "X")

car_2 = Car("Blue" , 75 , "Y")
Car.year = 2003

Car.display_year()
print(car_2.year)

car_1.display_info()
# Car.display_car_count()

Car.calculate_mileage(100 , 75)
