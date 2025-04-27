import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        if any(side <= 0 for side in (side1, side2, side3)):
            raise ValueError("All sides must be positive")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Invalid triangle sides: the sum of any two sides must be greater than the third side")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_angled(self, tolerance: float = 1e-7) -> bool:
        sides = sorted([self.side1, self.side2, self.side3])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tolerance

def calculate_area(shape: Shape) -> float:
    return shape.area()