# Compute whether an integer is even.
###################################################
# Is even formula
def is_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False


###################################################
# Test
def test(number):
    """Tests the is_even function."""
    if is_even(number):
        print number, "is even."
    else:
        print number, "is odd."

test(8)
test(3)
test(12)

# Compute whether a person is cool.
###################################################
# Is cool formula
def is_cool(name):
    if (name != "Scott"):
        return True
    else:
        return False


###################################################
# Test
def test(name):
    """Tests the is_cool function."""
    
    if is_cool(name):
        print name, "is cool."
    else:
        print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")

# Compute whether the given time is lunchtime.
###################################################
# Is lunchtime formula
def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hour == 12 and not is_am)


###################################################
# Test
def test(hour, is_am):
    """Tests the is_lunchtime function."""
    print hour,
    if is_am:
        print "AM",
    else:
        print "PM",
    if is_lunchtime(hour, is_am):
        print "is lunchtime."
    else:
        print "is not lunchtime."

test(11, True)
test(12, True)
test(11, False)
test(12, False)
test(10, False)

# Compute whether the given year is a leap year.
###################################################
# Is leapyear formula
# Student should enter function on the next lines.
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """	
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


###################################################
# Tests
def test(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2018)

# Compute whether two intervals intersect.
###################################################

def interval_intersect(a,b,c,d):
    """Formula: http://world.std.com/~swmcd/steven/tech/interval.html"""
    return (c <= a) and (b <= d)

###################################################
# Tests
def test(a, b, c, d):
    """Tests the interval_intersect function."""
    print "Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "]",
    if interval_intersect(a, b, c, d):
        print "intersect."
    else:
        print "do not intersect."

test(0, 1, 1, 2)
test(1, 2, 0, 1)
test(0, 1, 2, 3)
test(2, 3, 0, 1)
test(0, 3, 1, 2)

# Compute the statement about a person's name and age, given the person's name and age.
###################################################
# Name and age formula
def name_and_age(name, age):
    if age > 0:
        return str(name) + " is " + str(age) + " years old."
    else:
        return "Error: Invalid age"

###################################################
# Tests
def test(name, age):
    """Tests the name_and_age function."""
    
    print name_and_age(name, age)
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)

# Compute and print tens and ones digit of an integer in [0,100).
###################################################
# Digits function
def print_digits(num):    
    if num > 0 and num <= 100:
        tens = num // 10
        ones = num % 10
        print "The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + "."
    else:
        print "Error: Input is not a two-digit number."

    
###################################################
# Tests    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)

# Compute instructor's last name, given the first name.
###################################################
# Name lookup formula
def name_lookup(first_name):
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"


###################################################
# Tests
def test(first_name):
    """Tests the name_lookup function."""
    
    print name_lookup(first_name)
    
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")

