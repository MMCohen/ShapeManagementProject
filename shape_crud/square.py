from shape import Shape


class Square(Shape):
    def __init__(self,shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4

if __name__ == "__main__":
    s1 = Square(5, "square",5)
    assert s1.get_perimeter() == 20
    assert s1.get_area() == 25
    print(s1.get_perimeter())
    print(s1.get_area())