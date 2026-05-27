from shape import Shape


class Rectangle(Shape):
    def __init__(self,shape_id, shape_type, length, width):
        super().__init__(shape_id, shape_type)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
