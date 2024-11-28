class Circle:
    radius = 5

    def get_area (self):
        return 3.14 * (self.radius**2)
    
my_circle = Circle()

print(f"El radio del circulo es: {my_circle.radius} y el area del circulo es:{my_circle.get_area()}")