"""
Draw an indexed grid
"""

import simplegui

CELL_SIZE = 50
GRID_HEIGHT = 5
GRID_WIDTH = 4
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH

print "TOP"
for col in range(GRID_WIDTH):
    print [0, col]
    
print ""
print "BOTTOM"
for col in range(GRID_WIDTH):
    print [GRID_HEIGHT - 1, col]
    
print ""
print "LEFT"
for row in range(GRID_WIDTH):
    print [row, 0]
    
print ""
print "RIGHT"
for row in range(GRID_HEIGHT):
    print [row, GRID_WIDTH - 1]
    
# Handler to draw on canvas
def draw(canvas):
    """
    Draw the grid
    """
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            polygon = [[col * CELL_SIZE, row * CELL_SIZE], 
                       [col * CELL_SIZE, (row + 1) * CELL_SIZE], 
                       [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE], 
                       [(col + 1) * CELL_SIZE, (row) * CELL_SIZE]]
            canvas.draw_polygon(polygon, 1, "Black")
            text_pos = [(col + 0.1) * CELL_SIZE, (row + 0.8) * CELL_SIZE]
            canvas.draw_text(str(row) + "," + str(col), text_pos, 0.6 * CELL_SIZE, "Black")
                                
def run_gui(): 
    """
    Create a frame and assign draw handler
    """
    frame = simplegui.create_frame("Indexed grid", CANVAS_WIDTH, CANVAS_HEIGHT)
    frame.set_canvas_background("White")
    frame.set_draw_handler(draw)
    
    # Start the frame animation
    frame.start()

run_gui()