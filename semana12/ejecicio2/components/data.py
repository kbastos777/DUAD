from abc import ABC, abstractmethod


class Shape(ABC) :
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self):
        try:    
            self.radius = int(input("Please enter the circle radius:"))
        except ValueError as err:
            print(f"An error occurred due to: {err}")
            
    def calculate_perimeter(self):
        try:
            return 2*3.14 * self.radius
        except ValueError as err:
            print(f"An error occurred due to: {err}")
    
    def calculate_area(self):
        try:    
            return 3.14 * (self.radius**2)
        except ValueError as err:
            print(f"An error occurred due to: {err}")


class Square(Shape):
    def __init__(self):
        try:
            self.side = int(input("Please enter square side:"))
        except ValueError as err:
            print(f"An error occurred due to: {err}")
            
    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return (self.side**2)


class Rectangle(Shape):
    def __init__(self):
        try:
            self.length = int(input("Please enter the rectangle length:"))
            self.width =  int(input("Please enter the rectangle width:"))
        except ValueError as err:
            print(f"An error occurred due to: {err}")

    def calculate_perimeter(self):
        return 2*(self.length + self.width)
    
    def calculate_area(self):
        return self.length * self.width