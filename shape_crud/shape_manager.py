import logging
import json
from json import JSONDecodeError

from square import Square
from circle import Circle
from rectangle import Rectangle


class ShapeManager:
    def __init__(self):
        self.shapes: list[object] = []
        self.logger: logging.Logger = self.get_logger()
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
                self.logger.debug("created instance Square")

            case "circle": # todo:============================================
                radius = args
                temp_instance = Circle(shape_id, shape_type, radius, self.logger)
                self.shapes.append(temp_instance)
                self.logger.debug("created instance Circle")


            case "rectangle": # todo:============================================
                length, width = args
                temp_instance = Rectangle(shape_id, shape_type, length, width, self.logger)
                self.shapes.append(temp_instance)
                self.logger.debug("created instance Rectangle")


            case _:
                message = f"{shape_type} is not legal option"
                self.logger.error(message)
                raise ValueError(message)


    def get_all_shapes(self):
        """
        prints every shape detail using the print_shape_details method
        :return:
        """
        for shape_object in self.shapes:
            shape_object.print_shape_details()

        self.logger.info("done printing shapes details")

    def update_shape(self):
        pass

    def delete_shape(self):
        pass

    def save_to_json(self):
        pass

    def load_from_json(self):
        try:
            with open("shapes.json", "r", encoding="utf-8") as f:
                data = f.read()
                self.logger.debug("opened json file. data=%s", data)

                # checks that the json file is not empty:
                if not data:
                    self.logger.warning("json file was empty")
                    return []

                # else, convert json into list[dict]
                shapes_lst = json.loads(data)
                self.logger.info("converted json to list[dict] successfully")

        except JSONDecodeError:
            self.logger.error("not json format")
            raise

        self.logger.info("start to convert each item into Shape object")
        for shape in shapes_lst:
            shape_id, shape_type, *dimensions = shape.values()

            self.create_shape(shape_type, shape_id, dimensions) # todo:=================================================================
        self.logger.info("finish converting items to Shape objects")

        # just for testing
        self.logger.debug("list of objects=%s", self.shapes)
        return None

    def get_shape_id(self) -> int:
        """
        response on generating a new unique id.
        checks the max id in the shapes list
        and return the next one
        :return:
        """
        if self.shapes:
            return max([shape.shape_id for shape in self.shapes]) + 1
        return 1


    def get_logger(self) -> logging.Logger:
        logger1 = logging.getLogger(__name__)
        logger1.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("log_project.log", encoding="utf-8")
        formater = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

        file_handler.setFormatter(formater)
        logger1.addHandler(file_handler)

        return logger1


