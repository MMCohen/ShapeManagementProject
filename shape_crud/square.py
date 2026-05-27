from shape import Shape
import logging


class Square(Shape):
    """
    class Square Inherits form Shape class.
    implements the functions from Shape class
    """
    def __init__(self,shape_id, shape_type, side, logger: logging.Logger):
        super().__init__(shape_id, shape_type, logger)
        logger.info("create instance of Square | id=%s shape=%s side=%s ",shape_id, shape_type, side)
        self.side = side


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
            "side" : self.side
        }


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