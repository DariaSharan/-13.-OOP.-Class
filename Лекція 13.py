# Task 1. Create add method to add two countries together. 
# This method should create another country object with the name of the two countries combined and the population of the two countries added together.
# bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)
# bosnia_herzegovina = bosnia.add(herzegovina)
# bosnia_herzegovina.population -> 15_000_000
# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

# Creating two Country objects
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

# Adding the two countries together to create a new Country object
bosnia_herzegovina = bosnia.add(herzegovina)

# Accessing the attributes of the new Country object
print(bosnia_herzegovina.population)  # Output: 15000000
print(bosnia_herzegovina.name)        # Output: 'Bosnia Herzegovina'

# Task 2. Implement the previous method with a magic method
# bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)
# bosnia_herzegovina = bosnia + herzegovina
# bosnia_herzegovina.population -> 15_000_000
# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

# Creating two Country objects
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

# Using the magic method to add the two countries together and create a new Country object
bosnia_herzegovina = bosnia + herzegovina

# Accessing the attributes of the new Country object
print(bosnia_herzegovina.population)  # Output: 15000000
print(bosnia_herzegovina.name)        # Output: 'Bosnia Herzegovina'

# Task 3. Create a Car class with the following attributes: brand, model, year, and speed. 
# The Car class should have the following methods: accelerate, brake and display_speed. 
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5. 
# Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        print(f"The current speed of the {self.brand} {self.model} is {self.speed} km/h.")

# Create a Car instance
my_car = Car(brand='Toyota', model='Camry', year=2022)

# Display the initial speed
my_car.display_speed()  # Output: The current speed of the Toyota Camry is 0 km/h.

# Accelerate the car
my_car.accelerate()
my_car.display_speed()  # Output: The current speed of the Toyota Camry is 5 km/h.

# Accelerate again
my_car.accelerate()
my_car.display_speed()  # Output: The current speed of the Toyota Camry is 10 km/h.

# Brake the car
my_car.brake()
my_car.display_speed()  # Output: The current speed of the Toyota Camry is 5 km/h.

# Brake again
my_car.brake()
my_car.display_speed()  # Output: The current speed of the Toyota Camry is 0 km/h.

# Brake when the speed is already 0
my_car.brake()
my_car.display_speed()  # Output: The current speed of the Toyota Camry is 0 km/h.