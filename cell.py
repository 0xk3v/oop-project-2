"""
Module that holds cell class
"""


class Cell:
    """Cell class"""

    def __init__(self):
        # Cell status
        self.status = False

    def set_dead(self):
        self.status = False

    def set_alive(self):
        self.status = True

    def is_alive(self) -> bool:
        return self.status

    def get_symbol(self) -> str:
        if self.status:
            return ""
        else:
            # return ""
            return " "
