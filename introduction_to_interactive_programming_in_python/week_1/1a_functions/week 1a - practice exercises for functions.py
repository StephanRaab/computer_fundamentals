# Write a Python function miles_to_feet that takes a parameter miles and returns the number of feet in miles miles. 
def miles_to_feet(miles):
    total_feet =  miles * 5280
    return total_feet

miles_test = miles_to_feet(5)
print "The total distance is " + str(miles_test) + "ft."

# Write a Python function total_seconds that takes three parameters hours, minutes and seconds and returns the
# total number of seconds for hours hours, minutes minutes and seconds seconds.
def total_seconds(hours, minutes, seconds):
    hour_to_minute = hours * 60
    minutes_to_seconds = minutes * 60
    second_base = seconds
    total_time = hour_to_minute + minutes_to_seconds + second_base
    return total_time

time_test = total_seconds(4,24,55)
print time_test

# Write a Python function rectangle_perimeter that takes two parameters width and height corresponding to the
# lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.
def rectangle_perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter

perimeter_test = rectangle_perimeter(7, 4)
print perimeter_test

# Write a Python function rectangle_area that takes two parameters width and height corresponding to the
# lengths of the sides of a rectangle and returns the area of the rectangle in square inches.
def rectangle_area(width, height):
    area = width * height
    return area

area_test = rectangle_area(4, 34)
print area_test

# Write a Python function circle_circumference that takes a single parameter radius corresponding to the
# radius of a circle in inches and returns the the circumference of a circle with radius radius in inches.
# Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π.
import math

def circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

circumference_test = circle_circumference(7)
print circumference_test

# Write a Python function circle_area that takes a single parameter radius corresponding to the radius of
# a circle in inches and returns the the area of a circle with radius radius in square inches. Do not use
# π=3.14, instead use the math module to supply a higher-precision approximation to π.
import math

def circle_area(radius):
    area = math.pi * radius ** 2
    return area

circle_area_test = circle_area(4)
print circle_area_test

# Write a Python function future_value that takes three parameters present_value, annual_rate and years
# and returns the future value of present_value dollars invested at annual_rate percent interest, compounded
# annually for years years.
def future_value(present_value, annual_rate, years):
    #feel like a for loop is necessary here, so that we can add the percentage onto an increased number every year...
    annual_rate = annual_rate / 100
    future_value_total = present_value * annual_rate * years
    return future_value_total + present_value

future_value_test = future_value(30000, 4.2, 3)
print future_value_test

# Write a Python function name_tag that takes as input the parameters first_name and last_name (strings)
# and returns a string of the form "My name is % %." where the percents are the strings first_name and last_name.
# Reference the test cases in the provided template for an exact description of the format of the returned string.
def name_tag(first_name, last_name):
    full_name = first_name + " " + last_name
    return str("My name is ") + full_name

name_test = name_tag("Bo", "Burnham")
print name_test

# Write a Python function name_and_age that takes as input the parameters name (a string) and age (a number) and returns
# a string of the form "% is % years old." where the percents are the string forms of name and age.
# Reference the test cases in the provided template for an exact description of the format of the returned string.
def name_and_age(name, age):
    return name + str(" is ") + str(age) + " years old."

name_age_test = name_and_age("Jake", 24)
print name_age_test

# Write a Python function point_distance that takes as the parameters x0, y0, x1 and y1, and returns the distance
# between the points (x0,y0) and (x1,y1).
import math

def point_distance(x0, y0, x1, y1):
    distance = math.sqrt((x1-x0)**2 + (y1-y0)**2)
    return distance

distance_test = point_distance(2,3,2,-1)
print distance_test

# Write a Python function triangle_area that takes the parameters x0, y0, x1,y1, x2, and y2,
# and returns the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2).
# (Hint: use the function point_distance as a helper function and apply Heron's formula.)
import math

def triangle_area(x0, y0, x1, y1, x2, y2):
    a = point_distance(x0, y0, x1, y1)
    b = point_distance(x1, y1, x2, y2)
    c = point_distance(x2, y2, x0, y0)
    semi = (a + b + c)/ 2
    area = math.sqrt(semi * (semi - a) * (semi - b) * (semi - c))
    return area
    
triangle_area_test = triangle_area(2,3,2,-1,-1,-1)
print triangle_area_test

# Write a Python function print_digits that takes an integer number in the range [0,100),
# i.e., at least 0, but less than 100. It prints the message "The tens digit is %, and the ones digit is %.",
# where the percent signs should be replaced with the appropriate values. (Hint: Use the arithmetic operators
# for integer division // and remainder % to find the two digits. Note that this function should print the
# desired message, rather than returning it as a string.
def print_digits(int):
    tens = int // 10
    ones = int % 10
    
    if (int > 0 and int < 100):
        return "The tens digit is " + str(tens) + " and the ones digit is " + str(ones) + "."
    else: 
        return "Please try again with a number between 0 and 100."
print_digit_test = print_digits(37)
print print_digit_test

# Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery ticket
# with a specific number combination and, if the number on the ticket matches the numbers generated in a random
# drawing, the player wins a massive jackpot.
# Write a Python function powerball that takes no arguments and prints
# the message "Today's numbers are %, %, %, %, and %. The Powerball number is %.". The first five numbers should be
# random integers in the range [1,60), i.e., at least 1, but less than 60. In reality, these five numbers must
# all be distinct, but for this problem, we will allow duplicates. The Powerball number is a random integer
# in the range [1,36), i.e., at least 1 but less than 36. Use the random module and the function
# random.randrange to generate the appropriate random numbers.Note that this function should print the desired message,
# rather than returning it as a string
# My Version
import random

def powerball():    
    powerball_num = random.randrange(1, 36)
    today_slots = 5
    powerball_list = []
    while (today_slots > 0):
        num_generator = random.randrange(1, 60)
        powerball_list.append(num_generator)
        today_slots += -1
    
    print "Today's numbers are " + str(powerball_list[0:3]) + ", and " + str(powerball_list[4]) + "."
    print "The Powerball number is " + str(powerball_num) + "!"

powerball()

# Cameron's Version
# import random

# def powerball():
#     powerball_num = random.randrange(1, 36)
#     today_slots = 5
#     powerball_list = []

#     while (today_slots > 0):
#         num_generator = random.randrange(1, 60)
#         powerball_list.append(num_generator)
#         today_slots += -1

#     list_to_print = ', '.join(str(num) for num in powerball_list[0:4])
#     last_num = powerball_list[-1]

#     print("Today's numbers are {}, and {}.".format(list_to_print, last_num))
#     print("The Powerball number is {}".format(str(powerball_num) + "!"))

# powerball()