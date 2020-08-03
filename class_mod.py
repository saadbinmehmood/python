"""A class that can be used to represent a car."""
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

        
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    
    
class ElectricCars(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
class Resturants():
    def __init__(self, name, cusine_type):
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0
        
    def desc_rest (self):
        print(f"Resturant is \"{self.name}\" having an \"{self.cusine_type}\" cusine")
    def open_rest (self):
        print(f"\"{self.name}\" is still open")
    def set_number_served(self, update_number_served):
        self.number_served = update_number_served
    def incre_number_served(self, incre_number_served):
        self.number_served += incre_number_served

      
        
        
class User():
    def __init__(self, first_name, last_name, age, gender, profession):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.lower()
        self.profession = profession.title()
        self.login_attempts = 0
    def desc_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age} year old {self.gender} {self.profession}.")
    def greet_user(self):
        print(f"Welcome {self.profession} {self.first_name} {self.last_name}.")
    def incr_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
class Admin(User):
    def __init__(self,first_name, last_name, age, gender, profession):
        super().__init__(first_name, last_name, age, gender, profession)
        self.privilidges = "can add post", "can delete post", "can ban user-"
    
    def show_privilidges(self):
        print(f"The privilidges are {self.privilidges}")
        
        
        
class Privilidges():
    def __init__(self, privilidges=["can add post", "can delete post", "can ban user"]):
        self.privilidges = privilidges
        
    def show_privilidges(self):
        print(f"The privilidges are {self.privilidges}. Got it")