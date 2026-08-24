import math

class Triangle:
    def __init__(self, side1, side2, side3, angle1=0, angle2=0, angle3=0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        # All angles are 60 degrees
        super().__init__(side, side, side, 60, 60, 60)

    def calArea(self):
        area = (math.sqrt(3) / 4) * (self.side1 ** 2)
        return round(area)

    def find_angles(self):
        # Find tangent of angles in radians
        t1 = math.tan(math.radians(self.angle1))
        t2 = math.tan(math.radians(self.angle2))
        t3 = math.tan(math.radians(self.angle3))
        return t1, t2, t3

class Scalene(Triangle):
    def __init__(self, s1, s2, s3):
        super().__init__(s1, s2, s3)

    def calPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def calArea(self):
        s = self.calPerimeter() / 2
        # Heron's Formula
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return round(area)

# Test Equilateral
eq = EquilateralTriangle(6)
print("Equilateral Area:", eq.calArea())
print("Tangents of angles:", eq.find_angles())

# Test Scalene
sc = Scalene(5, 6, 7)
print("\nScalene Perimeter:", sc.calPerimeter())
print("Scalene Area:", sc.calArea())