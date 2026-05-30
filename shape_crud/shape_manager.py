import logging
import json
from json import JSONDecodeError

from square import Square
from circle import Circle
from rectangle import Rectangle


class ShapeManager:
    def __init__(self):
        self.json_file_name = "shapes.json"
        self.shapes: list[object] = []
        self.logger: logging.Logger = self.get_logger()
        self.load_from_json()


    def create_shape(self, shape_dict: dict): # todo: refactor to polimorphizem
        """
        gets dict with shape details. create an object.
        update both the self.shapes and the json.

        This function used both by the user from the main module
        and from the load_from_json() the convert the dicts into objects.

        :param shape_dict:
        :return:
        """
        new_shape = False
        # when converting json into object WILL NOT create a new id.
        # create shape id only for the user module.
        if not shape_dict.get("id"):
            new_shape = True
            shape_dict["id"] = self.get_shape_id()


        shape_id = shape_dict["id"]
        shape_type = shape_dict["type"]
        dimensions = shape_dict["dimensions"]

        # TODO: ===================================
        # I tried to send it directly to the class by:
        # class_name = shape_type.title()
        # class_name(shape_id, shape_type, self.logger, dimensions)
        # it did not work. for later

        self.logger.debug("try to create instance %s", shape_type)

        is_create_object = False

        match shape_type:
            case "square":
                temp_instance = Square(shape_id, shape_type, self.logger, dimensions)
                self.shapes.append(temp_instance)
                self.logger.debug("created instance %s successes", shape_type)
                is_create_object = True

            case "circle":
                temp_instance = Circle(shape_id, shape_type, self.logger, dimensions)
                self.shapes.append(temp_instance)
                self.logger.debug("created instance %s successes", shape_type)
                is_create_object = True

            case "rectangle":
                temp_instance = Rectangle(shape_id, shape_type, self.logger, dimensions)
                self.shapes.append(temp_instance)
                self.logger.debug("created instance %s successes", shape_type)
                is_create_object = True

            case _:
                message = f"{shape_type} is not legal option"
                self.logger.error(message)
                raise ValueError(message)

        if is_create_object:
            if new_shape:
                self.print_to_screen("shape added!")
            self.save_to_json()


    def get_all_shapes(self):
        """
        prints every shape detail using the print_shape_details method
        :return:
        """
        for shape_object in self.shapes:
            shape = shape_object.to_dict()
            self.print_to_screen(shape)

        self.logger.info("done printing shapes details")

    def update_shape(self, shape_id: int, dimensions: list):
        is_shape_id_in_shapes = False
        for idx, shape in enumerate(self.shapes):
            if shape.shape_id == shape_id:
                is_shape_id_in_shapes = True
                shape_dict = shape.to_dict()
                shape_dict["dimensions"] = dimensions
                self.delete_shape(shape_id)
                self.create_shape(shape_dict)
            if is_shape_id_in_shapes:
                break
        if is_shape_id_in_shapes:
            self.logger.info("shape updated")
        else:
            message = f"shape could NOT be update"
            self.logger.info(message)
            raise ValueError(message)


    def delete_shape(self, shape_id):
        is_shape_id_in_shapes = False
        shape_idx = ""
        for idx, shape in enumerate(self.shapes):
            if shape.shape_id == shape_id:
                is_shape_id_in_shapes = True
                shape_idx = idx
            if is_shape_id_in_shapes:
                break
        if is_shape_id_in_shapes:
            self.shapes.pop(shape_idx)
            self.save_to_json()
            self.print_to_screen("shape deleted!")

    def save_to_json(self):
        shapes_lst = []
        for shape in self.shapes:
            shapes_lst.append(shape.to_dict())
        if shapes_lst:
            with open(self.json_file_name, "w", encoding="utf-8") as f:
                json.dump(shapes_lst, f, indent=4)


    def load_from_json(self):
        try:
            with open(self.json_file_name, "r", encoding="utf-8") as f:
                data = f.read()
                self.logger.debug("opened json file. data=%s", data)

                # checks that the json file is not empty:
                if not data:
                    self.logger.warning("json file was empty")
                    return []

                # else, convert json into list[dict]
                shapes_lst = json.loads(data)
                self.logger.info("converted json to list[dict] successfully")

        except JSONDecodeError as e:
            self.logger.error("not json format | error= %s",e)
            raise

        except FileNotFoundError as e:
            self.logger.error("file not found | error= %s",e)
            raise

        self.logger.info("start to convert each item into Shape object")

        for shape in shapes_lst:
            self.create_shape(shape)

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


