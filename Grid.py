from copy import deepcopy

class Grid:
    """
    Represents a 2D grid data structure with (x, y) coordinate indexing.
    Manages internal state via a dynamically sized nested array.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for column in range(width)] for row in range(height)]

    def in_bounds(self, x, y):
        """
        Validates whether the specified (x, y) coordinates fall within the grid's
        dimensional boundaries. Returns a boolean.
        """
        if x >= self.width or y >= self.height:
            return False
        elif x < 0 or y < 0:
            return False
        else:
            return True

    def get(self, x, y):
        """
        Retrieves the value stored at the specified (x, y) coordinates.
        Raises an IndexError if the coordinates exceed grid bounds.
        """
        if self.in_bounds(x, y):
            wanted = self.array[y][x]
            return wanted
        else:
            raise IndexError("Out of bounds")

    def set(self, x, y, val):
        """
        Updates the matrix at the specified (x, y) coordinates with the provided value.
        Raises an IndexError if the coordinates exceed grid bounds.
        """
        if self.in_bounds(x, y):
            self.array[y][x] = val
        else:
            raise IndexError("Out of bounds")

    def __str__(self):
        return f'Grid({self.width}, {self.height}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid.build({self.array})'

    def __eq__(self, other):
        """
        Evaluates equality between this Grid instance and another Grid or
        nested list by comparing their internal array structures.
        """
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    @staticmethod
    def check_list_malformed(lst):
        """
        Validates the structural integrity of a nested list prior to Grid instantiation.
        Enforces non-empty, two-dimensional, uniformly sized constraints. Raises a
        ValueError if validation fails.
        """
        if isinstance(lst, list):
            if len(lst) == 0:
                raise ValueError("The top-level list should not be empty")
            for item in lst:
                if not isinstance(item, list):
                    raise ValueError("Each element of the list object should be a list object")
            equal_len = len(lst[0])
            for item in lst:
                if not len(item) == equal_len:
                    raise ValueError("Each element of the top-level list should have the same length")
        else:
            raise ValueError("The object passed in should be a list object")

    @staticmethod
    def build(lst):
        """
        Constructs and returns a new Grid instance from a validated nested list,
        utilizing a deep copy to ensure memory independence.
        """
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        new_grid = Grid(width, height)
        new_grid.array = deepcopy(lst)
        return new_grid

    def copy(self):
        """
        Returns a distinct, deep-copied instance of the current Grid object.
        """
        return deepcopy(self)