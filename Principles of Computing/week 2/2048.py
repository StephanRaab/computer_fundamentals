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

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        init_tiles = self._border[direction]
        rows = []
        columns = []

        #RIGHT
        if OFFSETS[direction] == (0,-1) or OFFSETS[direction] == (0,1):
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
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            temp5 = []
            row1 = rows[0:4]
            row2 = rows[4:8]
            row3 = rows[8:12]
            row4 = rows[12:16]
            row5 = rows[16:20]
            print row1
            print row2
            print row3
            print row4
            print row5
            for num in row1:
                temp1.append(self._grid[num[0]][num[1]])
            for num in row2:    
                temp2.append(self._grid[num[0]][num[1]])
            for num in row3:    
                temp3.append(self._grid[num[0]][num[1]])
            for num in row4:    
                temp4.append(self._grid[num[0]][num[1]])
            for num in row5:    
                temp5.append(self._grid[num[0]][num[1]])
                
            print temp1
            print temp2
            print temp3
            print temp4
            print temp5
            
            print "============"
            
            print merge(temp1)
            print merge(temp2)
            print merge(temp3)
            print merge(temp4)
            print merge(temp5)
        else:
            print "columns: ", columns
        
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
    
my_game = TwentyFortyEight(5, 4)
#my_game.reset()
#my_game.set_tile(0, 0, 2)
#my_game.set_tile(1, 0, 2)
#my_game.set_tile(0, 1, 2)
#my_game.set_tile(2, 1, 2)
#my_game.set_tile(0, 2, 2)
#my_game.set_tile(2, 2, 2)
#my_game.set_tile(1, 3, 2)
#my_game.set_tile(2, 3, 2)
#my_game.set_tile(2, 2, 4)
#my_game.set_tile(1, 2, 4)
#my_game.set_tile(1, 1, 4)
#print str(my_game)
#print my_game.get_tile(1, 2)
#my_game.new_tile()
#my_game.move(RIGHT)
print str(my_game)    
    
#poc_2048_gui.run_gui(TwentyFortyEight(5, 4))