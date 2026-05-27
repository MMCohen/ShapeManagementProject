from shape import Shape


class Circle(Shape):
    def __init__(self,shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self):
        return 3.1415 * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * self.radius * 3.1415

if __name__ == "__main__":
    c1 = Circle(1, "circle", 10)
    print(c1.get_perimeter())
    print(c1.get_area())