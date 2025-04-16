# sets the color variables
class colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (100, 100, 100)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    # class method to match the colors to the id of blocks
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.blue, cls.orange, cls.cyan, cls.yellow, cls.green, cls.purple, cls.red, cls.white, cls.dark_blue, cls.light_blue]

