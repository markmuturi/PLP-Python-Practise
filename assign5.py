# Activity 1
''' Create a class
    Add attributes and methods
    Use constructors to init objects with unique values
    Add an inheritance layer'''
class Car:
    def __init__(self, wheels):
        self.wheels = wheels
    
    def __init__(self, color):
        self.__color = color
        
    def __init__(self, model):
        self.__model = model
        
    def __init__(self, year):
        self.__year = year
        
        
# Activity 2
''' Program that includes animals or vehicles with the same action move()
    Make each class define move() differently'''
    
class Vehicle:
    def move(self):
        return "Driving"

class Animal:
    def move(self):
        return "Walking"
    
for item in [Vehicle(), Animal()]:
    print(item.move())
        


