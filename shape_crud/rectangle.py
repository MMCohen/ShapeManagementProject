from shape import Shape
import logging


class Rectangle(Shape):
    """
    class Rectangle Inherits form Shape class.
    implements the functions from Shape class
    """
    def __init__(self,shape_id, shape_type, length, width, logger: logging.Logger):
        super().__init__(shape_id, shape_type, logger)
        logger.info("create instance of Square | id=%s shape=%s length=%s width=%s",shape_id, shape_type, length, width)
        self.length = length
        self.width = width

    def get_area(self) -> int:
        """
        :return: the area of the rectangle
        """
        self.logger.info("get area | id=%s shape=%s length=%s width=%s",self.shape_id, self.shape_type, self.length, self.width)
        return self.length * self.width

    def get_perimeter(self) -> int:
        """
        :return: the perimeter of the rectangle
        """
        self.logger.info("get perimeter | id=%s shape=%s length=%s width=%s",self.shape_id, self.shape_type, self.length, self.width)

        return 2 * (self.length + self.width)

    def to_dict(self):
        """
        :return: dict with the info of the instance
        """
        self.logger.info("create dict | id=%s", self.shape_id)
        return {
            "id" : self.shape_id,
            "type" : self.shape_type,
            "length" : self.length,
            "width" : self.width
        }


    def print_shape_details(self):
        """
        prints the shape details
        :return:
        """
        shape_details = f"id={self.shape_id} shape={self.shape_type} length={self.length} width={self.width} area={self.get_area()} perimeter={self.get_perimeter()}"
        self.logger.debug("printing %s", shape_details)
        print(shape_details)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    r1 = Rectangle(1, "Rectangle", 10, 20, logger)
    assert r1.get_perimeter() == 60
    assert r1.get_area() == 200
    print(r1.get_perimeter())
    print(r1.get_area())
