from shape import Shape


class Square(Shape):
    def __init__(self, side, shape_id, shape_type):
        super().__init__(shape_id, shape_type)
        self.side = side
        self.shape_id = self.get_shape_id()  # todo: add function in Shape class
        self.type = "square"

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4