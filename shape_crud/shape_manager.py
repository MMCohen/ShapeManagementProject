import logging

from square import Square
from circle import Circle
from rectangle import Rectangle


class ShapeManager:
    def __init__(self):
        self.shapes: list[object] = []
        self.load_from_json()

    def create_shape(self, shape):
        pass

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