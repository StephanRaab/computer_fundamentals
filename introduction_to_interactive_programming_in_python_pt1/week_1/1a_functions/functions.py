#computes the area of a triangle
def triangle_area(base, height):
    area = (1.0/2) * base * height
    return area

a1 = triangle_area(3, 2)
print a1

#converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0/9) * (fahrenheit - 32)
    return celsius

#test
celsius1 = fahrenheit2celsius(72)
print celsius1

#convert fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

#test kelvin
k1 = fahrenheit2kelvin(32)
print k1

#prints hello, world
def hello():
    print "Hello, world!"

#test hello
hello()
