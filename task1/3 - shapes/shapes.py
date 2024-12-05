import math

class Shapes:
    def area(im):
        raise NotImplementedError

    def perimeter(im):
        raise NotImplementedError

    def compare_area(im, notim):
        return im.area() > notim.area()

    def compare_perimeter(im, notim):
        return im.perimeter() > notim.perimeter()
		
class Square(Shapes):
    def __init__(im, iside):
        im.iside = iside

    def area(im):
        return im.iside ** 2

    def perimeter(im):
        return 4 * im.iside
		
class Rectangle(Shapes):
    def __init__(im, width, height):
        im.width = width
        im.height = height

    def area(im):
        return im.width * im.height

    def perimeter(im):
        return 2 * (im.width + im.height)
		
class Triangle(Shapes):
    def __init__(im, a, b, c):
        im.a = a
        im.b = b
        im.c = c

    def area(im): # Heron's formula
        s = (im.a + im.b + im.c) / 2
        return math.sqrt(s * (s - im.a) * (s - im.b) * (s - im.c))

    def perimeter(im):
        return im.a + im.b + im.c

class Circle(Shapes):
    def __init__(im, r):
        im.r = r

    def area(im):
        return math.pi * im.r ** 2

    def perimeter(im):
        return 2 * math.pi * im.r
		
square = Square(7)
rectangle = Rectangle(6, 8)
triangle = Triangle(3, 4, 5)
circle = Circle(6)

print(square.area())       # 49
print(square.perimeter())  # 28

print(rectangle.area())    # 48
print(rectangle.perimeter())  # 28

print(triangle.area())    # 6
print(triangle.perimeter())  # 12

print(circle.area())      # 113.09733552923255
print(circle.perimeter())  # 37.69911184307752

print(square.compare_area(rectangle))
print(square.compare_perimeter(rectangle))