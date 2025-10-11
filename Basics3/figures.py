import math
import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self) -> float:
        pass
    
    @abc.abstractmethod
    def calculate_perimeter(self) -> float:
        pass

class Comparison:
    @staticmethod
    def compare_figures(value1: float, value2: float) -> str:
        if value1 > value2:
            return "Больше"
        elif value1 < value2:
            return "Меньше"
        return "Равны"

class Rectangle(Figure, Comparison):
    def __init__(self, height: float, width: float) -> None:
        self.height: float = height
        self.width: float = width

    def calculate_area(self) -> float:
        return self.height * self.width
    
    def calculate_perimeter(self) -> float:
        return (self.height + self.width) * 2
    
    def compare_area(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_area(), other.calculate_area())
    
    def compare_perimeter(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_perimeter(), other.calculate_perimeter())

class Square(Figure, Comparison):
    def __init__(self, side: float) -> None:
        self.side: float = side

    def calculate_area(self) -> float:
        return self.side ** 2 
    
    def calculate_perimeter(self) -> float:
        return self.side * 4
    
    def compare_area(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_area(), other.calculate_area())
    
    def compare_perimeter(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_perimeter(), other.calculate_perimeter())

class Circle(Figure, Comparison):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def compare_area(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_area(), other.calculate_area())
    
    def compare_perimeter(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_perimeter(), other.calculate_perimeter())

class Triangle(Figure, Comparison):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def calculate_perimeter(self) -> float: 
        return self.a + self.b + self.c
    
    def calculate_area(self) -> float:
        p = self.calculate_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def compare_area(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_area(), other.calculate_area())
    
    def compare_perimeter(self, other: Figure) -> str:
        return self.compare_figures(self.calculate_perimeter(), other.calculate_perimeter())

rectangle: Rectangle = Rectangle(2, 6)
square: Square = Square(4)
circle: Circle = Circle(3)
triangle: Triangle = Triangle(3, 4, 5)

print("Площадь прямоугольника:", rectangle.calculate_area(), "Периметр прямоугольника:", rectangle.calculate_perimeter())
print("Площадь квадрата:", square.calculate_area(), "Периметр квадрата:", square.calculate_perimeter())
print("Площадь окружности:", circle.calculate_area(), "Периметр окружности:", circle.calculate_perimeter())
print("Площадь треугольника:", triangle.calculate_area(), "Периметр треугольника:", triangle.calculate_perimeter())

print("Площадь квадрата против прямоугольника:", square.compare_area(rectangle))
print("Периметр квадрата против прямоугольника:", square.compare_perimeter(rectangle))