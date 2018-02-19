"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

top_border = []
bottom_border = []
left_border = []
right_border = []

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    first_list = []
    for num in line:
        if num  > 0:
            first_list.append(num)
    if len(first_list) < len(line):
        add_zero = len(line) - len(first_list)
        for num in range(add_zero):
            first_list.append(0)
         
    for num in range(1, len(line)):
        if first_list[num - 1] == first_list[num]:
            first_list[num - 1] *= 2
            first_list[num] = 0
    
    final_list = []
    for num in first_list:
        if num > 0:
            final_list.append(num)
    if len(final_list) < len(line):
        add_zero = len(line) - len(final_list)
        for num in range(add_zero):
            final_list.append(0)
            
    return final_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.height = grid_height
        self.width = grid_width
        self.reset()
        for col in range(self.width):
            top_border.append([0, col])

        for col in range(self.width):
            bottom_border.append([self.height - 1, col])

        for row in range(self.height):
            left_border.append([row, 0])

        for row in range(self.height):
            right_border.append([row, self.width - 1])
        
        self.border = {UP: top_border, DOWN: bottom_border,
                       LEFT: left_border, RIGHT: right_border}

    def reset(self):
        """
        Reset the game so the grid is empty, generate two
        initial tiles.
        """
        # set entire grid to zeros
        self.grid = [[0 for col in range(self.get_grid_width())] 
                   for row in range(self.get_grid_height())]
        
        # generate two new tiles
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "\n".join([str(row) for row in self.grid])
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        num_steps = 0
        init_tiles = self.border[direction]
        rows = []
        columns = []

        if OFFSETS[direction] == (0,1) or OFFSETS[direction] == (0,-1):
            num_steps = self.get_grid_width()
            for row in init_tiles:
                for col in range(num_steps):
                    rows.append([row[0], col])

        else:
            num_steps = self.get_grid_height()
            for row in init_tiles:
                for col in range(num_steps):
                    columns.append([col, row[1]])
        
        if len(rows) > 0:
            print "rows: ", rows
        else:
            print "columns: ", columns

        print self.grid[0][0]
        print self.grid[1][0]
        print self.grid[2][0]
        print self.grid[3][0]
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if random.random() <= 0.9:
            new_tile_num = 2
        else:
            new_tile_num = 4
        
        open_tiles = [(row, col) for row in range(self.get_grid_height())
                       for col in range(self.get_grid_width()) if self.get_tile(row,col) == 0]
                                        
        if len(open_tiles) != 0:
            (row, col) = random.choice(open_tiles)
            self.set_tile(row, col, new_tile_num)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]
    
poc_2048_gui.run_gui(TwentyFortyEight(5, 4))