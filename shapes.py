from math import pi, tan, sqrt

# Classes below model only set of shapes given in the task and I didn't assume future extension.

class Rectangle:
    # As a base class I assumed rectangle with its 2 dimensions, that can be used for other shapes.
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length = 0):
        super().__init__(length, length)

class Cube(Square):
    def calculate_area(self):
        return super().calculate_area() * 6
    def calculate_volume(self):
        return super().calculate_area() * self.length

class Triangle(Rectangle):
    # In case of triangle 'width' is identical as 'height' in common understanding.
    def calculate_area(self):
        return 0.5 * self.length * self.width

class Oval(Rectangle):
    # I assumed that oval is the same as ellipse and length and width represents a major and a minor radius.
    def calculate_area(self):
        return round(pi * self.length * self.width, 2)

class RegularPyramid:
    # Regular pyramid is described by 3 variables: side "length", n-gonal base "sidesnumber" and "height" of pyramid.
    def __init__(self, length = 0, sidesnumber = 0, height = 0):
        self.length = length
        self.sidesnumber = sidesnumber
        self.height = height

    def calculate_radius(self):
    # This method calculates the radius of a pyramid base (polygons's) in-circle.
        return round(self.length / 2 * 1 / tan(pi / self.sidesnumber), 4)

    def calculate_base_area(self):
        return round(self.sidesnumber * self.length / 2 * self.calculate_radius(), 2)

    def calculate_sides_area(self):
        slant_height = sqrt(self.calculate_radius() ** 2 + self.height ** 2)
        return round(self.sidesnumber * self.length * slant_height / 2, 2)

    def calculate_area(self):
        return self.calculate_base_area() + self.calculate_sides_area()

    def calculate_volume(self):
        return round(self.height / 3 * self.calculate_base_area(), 2)

calculated = ['Area', 'Volume']
output_text = '{} of {} with dimensions {} by {} is: {}'
output_text_pyramid = '{} of {} with base of {} sides with length of {} and height {} is: {}'


rectangle = Rectangle(2,5)
print(output_text.format(calculated[0], rectangle.__class__.__name__, rectangle.length, rectangle.width, \
                         rectangle.calculate_area()))

square = Square(5)
print(output_text.format(calculated[0], square.__class__.__name__, square.length, square.width, \
                         square.calculate_area()))

cube = Cube(3)
print(output_text.format(calculated[0], cube.__class__.__name__, cube.length, cube.width, cube.calculate_area()))
print(output_text.format(calculated[1], cube.__class__.__name__, cube.length, cube.width, cube.calculate_volume()))

triangle = Triangle(4,3)
print(output_text.format(calculated[0], triangle.__class__.__name__,triangle.length, triangle.width, \
                         triangle.calculate_area()))

oval = Oval(4,3)
print(output_text.format(calculated[0], oval.__class__.__name__,oval.length, oval.width, oval.calculate_area()))

pyramid = RegularPyramid(4,3,5)
print(output_text_pyramid.format(calculated[0], pyramid.__class__.__name__, pyramid.length, pyramid.sidesnumber, \
                                 pyramid.height, pyramid.calculate_area()))
print(output_text_pyramid.format(calculated[1], pyramid.__class__.__name__, pyramid.length, pyramid.sidesnumber, \
                                 pyramid.height, pyramid.calculate_volume()))
