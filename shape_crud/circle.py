from shape import Shape


class Circle(Shape):
    """
    class Circle Inherits form Shape class.
    implements the functions from Shape class
    """
    PI = 3.1415
    def __init__(self,shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self) -> int:
        """
        :return: the area of the circle
        """
        return Circle.PI * (self.radius ** 2)

    def get_perimeter(self) -> int:
        """
        :return: the perimeter of the circle
        """
        return 2 * self.radius * Circle.PI

if __name__ == "__main__":
    c1 = Circle(1, "circle", 10)
    print(c1.get_perimeter())
    print(c1.get_area())