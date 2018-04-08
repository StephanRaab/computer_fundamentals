"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        self.obstacle_list = []
        self.zombie_list = []
        self.human_list = []
        
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._zombie_list = []
        self._human_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)  
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        
#        Create a new grid 𝚟𝚒𝚜𝚒𝚝𝚎𝚍 of the same size as the original grid
#        and initialize its cells to be empty.
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        
#    	Create a 2D list 𝚍𝚒𝚜𝚝𝚊𝚗𝚌𝚎_𝚏𝚒𝚎𝚕𝚍 of the same size as the original
#        grid and initialize each of its entries to be the product of the
#        height times the width of the grid.
#        (This value is larger than any possible distance.)
        distance_field = [[self._grid_height * self._grid_width for dummy_column in range(self._grid_width)]
                           for dummy_row in range(self._grid.height)]
    
#    	Create a queue 𝚋𝚘𝚞𝚗𝚍𝚊𝚛𝚢 that is a copy of either the zombie list or the human list.
#        For cells in the queue, initialize 𝚟𝚒𝚜𝚒𝚝𝚎𝚍 to be 𝙵𝚄𝙻𝙻 and 𝚍𝚒𝚜𝚝𝚊𝚗𝚌𝚎_𝚏𝚒𝚎𝚕𝚍 to be zero.
#        We recommend that you use our 𝚀𝚞𝚎𝚞𝚎 class.

        boundary = poc.queue.Queue()
    
        if entity_type == ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        if entitiy_type == HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
                
#        while boundary is not empty:
        while len(boundary) > 0:
#           current_cell  ←  dequeue boundary
            current_cell = boundary.dequeue()
    #        for all neighbor_cell of current_cell:
            neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            for neighbor_cell in neighbors: 
    #            if neighbor_cell is not in visited:
                if neighbor_cell.is_empty(neighbor_cell[0], neighbor_cell[1]) and self.is_empty(neighbor[0], neighbor[1]):
    #                add neighbor_cell to visited
                    visited.set_full(neighbor_cell[0], neighbor_cell[1])
    #                enqueue neighbor_cell onto boundary
                    boundary.enqueue(neighbor_cell)
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = \
                        distance_field[current_cell[0]][current_cell[1]] + 1
        
        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        pass
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        pass

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#newZombie = Apocalypse(6,6)
#print newZombie.add_human(0,1)
#print newZombie.add_human(0,2)
#print newZombie.add_human(2,4)
#print newZombie.num_humans()
#print newZombie.humans()

poc_zombie_gui.run_gui(Apocalypse(30, 40))
