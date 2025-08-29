# Assignment 1: Design Your Own Class

# Let’s design a Smartphone class, then extend it with an iPhone and AndroidPhone subclass to explore inheritance and polymorphism.

#  Smartphone Class 

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # encapsulated (private) attribute
        self.__battery = battery  
        self.brand = brand
        self.model = model
        self.storage = storage

    # method to show phone details
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

    # method to simulate charging
    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged to {self.__battery}%"

    # getter method (encapsulation)
    def get_battery(self):
        return self.__battery


# Inheritance: iPhone class
class iPhone(Smartphone):
    def __init__(self, model, storage, battery, ios_version):
        super().__init__("Apple", model, storage, battery)
        self.ios_version = ios_version

    def phone_info(self):
        return f"iPhone {self.model}, iOS {self.ios_version}, {self.storage}GB"


# Inheritance: AndroidPhone class
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        super().__init__(brand, model, storage, battery)
        self.android_version = android_version

    def phone_info(self):
        return f"{self.brand} {self.model}, Android {self.android_version}, {self.storage}GB"


# Activity 2: Polymorphism Challenge

# classic Animal polymorphism with move() behaving differently.

class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")


class Dog(Animal):
    def move(self):
        return "Running"


class Fish(Animal):
    def move(self):
        return "Swimming"


class Bird(Animal):
    def move(self):
        return "Flying"


















