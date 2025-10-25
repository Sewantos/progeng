import math
import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self) -> float:
        pass
    
    @abc.abstractmethod
    def calculate_perimeter(self) -> float:
        pass
    
class Comparison(Figure, abc.ABC):
    def get_measure(self, compare_by: str) -> float:
        if compare_by == 'area':
            return self.calculate_area()
        elif compare_by == 'perimeter':
            return self.calculate_perimeter()
        raise ValueError("compare_by must be 'area' or 'perimeter'")
    
    def is_greater(self, other: Figure, compare_by: str = 'area') -> bool:
        return self.get_measure(compare_by) > other.get_measure(compare_by)
    
    def is_less(self, other: Figure, compare_by: str = 'area') -> bool:
        return self.get_measure(compare_by) < other.get_measure(compare_by)
    
    def are_equal(self, other: Figure, compare_by: str = 'area') -> bool:
        return math.isclose(
            self.get_measure(compare_by), other.get_measure(compare_by)
        )

class Rectangle(Comparison):
    def __init__(self, height: float, width: float) -> None:
        self.height: float = height
        self.width: float = width

    def calculate_area(self) -> float:
        return self.height * self.width
    
    def calculate_perimeter(self) -> float:
        return (self.height + self.width) * 2
       
class Square(Comparison):
    def __init__(self, side: float) -> None:
        self.side: float = side

    def calculate_area(self) -> float:
        return self.side ** 2 
    
    def calculate_perimeter(self) -> float:
        return self.side * 4
    
class Circle(Comparison):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Triangle(Comparison):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def calculate_perimeter(self) -> float: 
        return self.a + self.b + self.c
    
    def calculate_area(self) -> float:
        p = self.calculate_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
rectangle: Rectangle = Rectangle(2, 6)
square: Square = Square(4)
circle: Circle = Circle(3)
triangle: Triangle = Triangle(3, 4, 5)

print(
    "Площадь прямоугольника:", rectangle.calculate_area(),
    "Периметр прямоугольника:", rectangle.calculate_perimeter()
)
print(
    "Площадь квадрата:", square.calculate_area(),
    "Периметр квадрата:", square.calculate_perimeter()
)
print(
    "Площадь окружности:", circle.calculate_area(),
    "Периметр окружности:", circle.calculate_perimeter()
)
print(
    "Площадь треугольника:", triangle.calculate_area(),
    "Периметр треугольника:", triangle.calculate_perimeter()
)

print(
    "Площадь квадрата больше площади прямоугольника:",
    square.is_greater(rectangle, compare_by='area')
)
print(
    "Площадь квадрата меньше площади прямоугольника:",
    square.is_less(rectangle, compare_by='area')
)
print(
    "Периметр квадрата больше периметра прямоугольника:",
    square.is_greater(rectangle, compare_by='perimeter')
)
print(
    "Периметр квадрата меньше периметра прямоугольника:",
    square.is_less(rectangle, compare_by='perimeter')
)
print(
    "Периметр квадрата равен периметру прямоугольника:",
    square.are_equal(rectangle, compare_by='perimeter')
)
