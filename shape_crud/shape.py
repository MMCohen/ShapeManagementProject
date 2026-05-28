import logging


class Shape:
    def __init__(self, shape_id, shape_type, logger: logging.Logger):
        self.shape_id = shape_id
        self.shape_type = shape_type
        if not isinstance(logger, logging.Logger):
            raise ValueError("loger must be Logger type")
        self.logger = logger

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def to_dict(self):
        pass

    def print_shape_details(self):
        pass