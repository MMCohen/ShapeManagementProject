from shape import Shape


class Rectangle(Shape):
    """
    class Rectangle Inherits form Shape class.
    implements the functions from Shape class
    """
    def __init__(self,shape_id, shape_type, length, width):
        super().__init__(shape_id, shape_type)
        self.length = length
        self.width = width

    def get_area(self) -> int:
        """
        :return: the area of the rectangle
        """
        return self.length * self.width

    def get_perimeter(self) -> int:
        """
        :return: the perimeter of the rectangle
        """
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    r1 = Rectangle(1, "Rectangle", 10, 20)
    assert r1.get_perimeter() == 60
    assert r1.get_area() == 200
    print(r1.get_perimeter())
    print(r1.get_area())
