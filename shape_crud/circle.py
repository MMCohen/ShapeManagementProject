from shape import Shape
import logging


class Circle(Shape):
    """
    class Circle Inherits form Shape class.
    implements the functions from Shape class
    """
    PI = 3.1415
    def __init__(self,shape_id, shape_type, logger: logging.Logger, dimensions):
        super().__init__(shape_id, shape_type, logger)
        logger.info("create instance of circle | id=%s shape=%s radius=%s ",shape_id, shape_type, dimensions)
        self.radius = dimensions[0]

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


    def print_shape_details(self):
        """
        prints the shape details
        :return:
        """
        shape_details = f"id={self.shape_id} shape={self.shape_type} radius={self.radius} area={self.get_area()} perimeter={self.get_perimeter()}"
        self.logger.debug("printing %s", shape_details)
        print(shape_details)


if __name__ == "__main__":
    c1 = Circle(1, "circle", 10)
    print(c1.get_perimeter())
    print(c1.get_area())