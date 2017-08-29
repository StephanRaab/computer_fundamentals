import simplegui

# initialize global variables
store = 0
operand = 0

# define functions that manipulate store and operand


def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""

def swap():
    global store, operand
    store, operand = operand, store
    output()

def add():
    global store, operand
    store = store + operand
    output()

def subtract():
    global store, operand
    store = store - operand
    output()

def multiply():
    global store, operand
    store = store * operand
    output()

def divide():
    global store, operand
    store = store / operand
    output()

def enter(input):
    """make sure to convert str to float"""
    global operand
    operand = float(input)
    output()

frame = simplegui.create_frame('Calculator', 300, 300)

frame.add_button('Print', output, 100)
frame.add_button('Swap', swap, 100)
frame.add_button('Add', add, 100)
frame.add_button('Subtract', subtract, 100)
frame.add_button('Multiply', multiply, 100)
frame.add_button('Divide', divide, 100)
inp = frame.add_input('Enter', enter, 100)

frame.start()