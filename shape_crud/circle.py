from shape import Shape
import logging


class Circle(Shape):
    """
    class Circle Inherits form Shape class.
    implements the functions from Shape class
    """
    PI = 3.1415
    def __init__(self,shape_id, shape_type, radius, logger: logging.Logger):
        super().__init__(shape_id, shape_type, logger)
        logger.info("create instance of circle | id=%s shape=%s radius=%s ",shape_id, shape_type, radius)
        self.radius = radius

    def get_area(self) -> int:
        """
        :return: the area of the circle
        """

        self.logger.info("get area | id=%s shape=%s radius=%s ",self.shape_id, self.shape_type, self.radius)

        return Circle.PI * (self.radius ** 2)

    def get_perimeter(self) -> int:
        """
        :return: the perimeter of the circle
        """
        self.logger.info("get perimeter | id=%s shape=%s radius=%s ",self.shape_id, self.shape_type, self.radius)
        return 2 * self.radius * Circle.PI

    def to_dict(self):
        """
        :return: dict with the info of the instance
        """
        self.logger.info("create dict | id=%s", self.shape_id)
        return {
            "id" : self.shape_id,
            "type" : self.shape_type,
            "radius" : self.radius
        }

if __name__ == "__main__":
    c1 = Circle(1, "circle", 10)
    print(c1.get_perimeter())
    print(c1.get_area())