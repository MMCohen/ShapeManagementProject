import logging

from square import Square
from circle import Circle
from rectangle import Rectangle


class ShapeManager:
    def __init__(self):
        self.shapes: list[object] = []
        self.logger: logging.Logger = self.get_logger() # todo: =============================
        self.load_from_json()

    def create_shape(self,shape_type, shape_id = None, *args):
        """
        gets the chosen shape and the dimensions
        This function can be used both by the user from the main module
        and the load_from_json() the convert the dicts into objects.

        :param shape_id:
        :param shape_type:
        :param args:
        :return:
        """
        # when converting json into object WILL NOT create a new id.
        # create shape id only for the user module.
        if not shape_id:
            shape_id = self.get_shape_id()

        match shape_type:
            case "square":
                side = args
                temp_instance = Square(shape_id, shape_type, side, self.logger)
                self.shapes.append(temp_instance)

            case "circle":
                pass
            case "rectangle":
                pass
            case _:
                raise ValueError(f"{shape_type} is not legal option")


    def get_all_shapes(self):
        pass

    def update_shape(self):
        pass

    def delete_shape(self):
        pass

    def save_to_json(self):
        pass

    def load_from_json(self):
        pass