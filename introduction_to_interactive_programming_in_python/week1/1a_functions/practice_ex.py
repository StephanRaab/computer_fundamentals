# Function miles_to_feet
def miles_to_feet(miles):
    distance = str(miles * 5280) + "ft"
    return distance

miles2feettest = miles_to_feet(20)
print miles2feettest

# Function total_seconds
def total_seconds(hour, minute, second):
    hour = minute * 60
    minute = second * 60
    second = 1
    total = str(hour) + str(minute) + str(second) + " total seconds"
    return total

secondtest = total_seconds(2,6,2)
print secondtest

# Function rectangle_perimeter
def rectangle_perimeter(width, height):
    perimeter = 2 * (height + width)
    return perimeter

perimeterTest = rectangle_perimeter(5, 7)
print "The perimeter is " + str(perimeterTest)
