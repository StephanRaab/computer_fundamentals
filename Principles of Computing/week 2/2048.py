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

T_BORDER = []
B_BORDER = []
L_BORDER = []
R_BORDER = []

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
        self._height = grid_height
        self._width = grid_width
        self.reset()
        for col in range(self._width):
            T_BORDER.append([0, col])

        for col in range(self._width):
            B_BORDER.append([self._height - 1, col])

        for row in range(self._height):
            L_BORDER.append([row, 0])

        for row in range(self._height):
            R_BORDER.append([row, self._width - 1])
        
        self._border = {UP: T_BORDER, DOWN: B_BORDER,
                       LEFT: L_BORDER, RIGHT: R_BORDER}

    def reset(self):
        """
        Reset the game so the grid is empty, generate two
        initial tiles.
        """
        # set entire grid to zeros
        self._grid = [[0 for num in range(self.get_grid_width())] 
                   for num in range(self.get_grid_height())]
        
        # generate two new tiles
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "\n".join([str(row) for row in self._grid])
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
    
    def traverse_grid(self, start_cell, direction, num_steps, moved):
        """
        Function that iterates through the cells in a grid
        in a linear direction

        Both start_cell is a tuple(row, col) denoting the
        starting cell

        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        #temp list for merge function
        temp_list = []

        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            temp_list.append(self._grid[row][col])
        new_list = merge(temp_list)

        # store new list into grid
        new_list_count = 0
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]

            # compare new with old cells
            if new_list[new_list_count] != self._grid[row][col]:
                moved = True
            self._grid[row][col] = new_list[new_list_count]          
            new_list_count += 1
        return moved
                                              
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved = False
        if direction == UP:
            for num in self._border[UP]:
                moved = self.traverse_grid(num, OFFSETS[UP], self._height, moved)
        elif direction == DOWN:
            for num in self._border[DOWN]:
                moved = self.traverse_grid(num, OFFSETS[DOWN], self._height, moved)
        elif direction == LEFT:
            for num in self._border[LEFT]:
                moved = self.traverse_grid(num, OFFSETS[LEFT], self._width, moved)
        elif direction == RIGHT:
            for num in self._border[RIGHT]:
                moved = self.traverse_grid(num, OFFSETS[RIGHT], self._width, moved)
        if moved:
            self.new_tile() 
        
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
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col] 
    
obj = TwentyFortyEight(4, 4)
obj.set_tile(0, 0, 2)
obj.set_tile(0, 1, 0)
obj.set_tile(0, 2, 0)
obj.set_tile(0, 3, 0)
obj.set_tile(1, 0, 0)
obj.set_tile(1, 1, 2)
obj.set_tile(1, 2, 0)
obj.set_tile(1, 3, 0)
obj.set_tile(2, 0, 0)
obj.set_tile(2, 1, 0)
obj.set_tile(2, 2, 2)
obj.set_tile(2, 3, 0)
obj.set_tile(3, 0, 0)
obj.set_tile(3, 1, 0)
obj.set_tile(3, 2, 0)
obj.set_tile(3, 3, 2)
print str(obj)
print "============"
obj.move(DOWN)
#expected:
#[[0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [2, 2, 2, 2]] 
print str(obj)
#poc_2048_gui.run_gui(TwentyFortyEight(5, 4))