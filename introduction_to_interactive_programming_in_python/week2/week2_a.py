# Printing "Goodbye" with a local message variable
###################################################
# Student should enter function on the next lines.
def print_goodbye():
    message = "Goodbye"
    print(message)

###################################################
# Tests
message = "Hello"
print(message)
print_goodbye()
print(message)

message = "Ciao"
print(message)
print_goodbye()
print(message)

print("###########################################")

# Printing "Goodbye" with a global message variable
###################################################
# Student should enter function on the next lines.
def set_goodbye():
    global message
    message = "Goodbye"
    print(message)

###################################################
# Tests
message = "Hello"
print(message)
set_goodbye()
print(message)

message = "Ciao"
print(message)
set_goodbye()
print(message)

print("###########################################")

# Functions to manipulate global variable count
###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.
def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    global count
    print(count)


###################################################
# Test
# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

print("###########################################")
