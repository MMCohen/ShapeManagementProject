from shape import Shape
import logging


class Square(Shape):
    """
    class Square Inherits form Shape class.
    implements the functions from Shape class
    """
    def __init__(self,shape_id, shape_type, logger: logging.Logger, dimensions):
        super().__init__(shape_id, shape_type, logger)
        logger.info("create instance of Square | id=%s shape=%s side=%s ",shape_id, shape_type, dimensions)
        self.side = dimensions[0]


    def get_area(self) -> int:
        """
        :return: the area of the square calculate by side * side
        """

        self.logger.info("get area | id=%s shape=%s side=%s ",self.shape_id, self.shape_type, self.side)

        return self.side * self.side


    def get_perimeter(self) -> int:
        """
        :return: the perimeter of the square
        """

        self.logger.info("get perimeter | id=%s shape=%s side=%s ",self.shape_id, self.shape_type, self.side)

        return self.side * 4

    def to_dict(self):
        """
        :return: dict with the info of the instance
        """
        self.logger.info("create dict | id=%s", self.shape_id)
        return {
            "id" : self.shape_id,
            "type" : self.shape_type,
            "dimensions" : [self.side]
        }

    def print_shape_details(self):
        """
        prints the shape details
        :return:
        """
        shape_details = f"id={self.shape_id} shape={self.shape_type} side={self.side} area={self.get_area()} perimeter={self.get_perimeter()}"
        self.logger.debug("printing %s", shape_details)
        print(shape_details)

if __name__ == "__main__":
    #create test loger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    s1 = Square(5, "square",5, logger)
    assert s1.get_perimeter() == 20
    assert s1.get_area() == 25

    print(s1.get_perimeter())
    print(s1.get_area())
    print(s1.to_dict())