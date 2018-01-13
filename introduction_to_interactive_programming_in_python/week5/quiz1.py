#list = [2, 5, 8, 11, 14]
#
#print range(14, 1, -3)
#print range(2, 17, 3)
#print range(2, 14, 3)

#numbers = [5,2,3]
#product = 1
#
#for n in numbers:
#    product *= n
#    print product

#def reverse_string(s):
#    """Returns the reversal of the given string."""
#    result = ""
#    for char in s:
#        result = char + result
#    return result
#
#print reverse_string("ola")

#import random
#
#def random_point():
#    """Returns a random point on a 100x100 grid."""
#    return (random.randrange(100), random.randrange(100))
#
#def starting_points(players):
#    """Returns a list of random points, one for each player."""
#    points = []
#    for player in players:
#        point = random_point()
#        points.append(point)
#    return points
#
#players = ["jack", "jill", "Stephan"]
#print starting_points(players)

#numbers1 = [2,6,9,12,400] # True
#numbers2 = [4, 8, 2, 12] #False
#
#def is_ascending(numbers):
#    """Returns whether the given list of numbers is in ascending order."""
#    for i in range(len(numbers)-1):
#        if numbers[i+1] < numbers[i]:
#            return False
#    return True
#
#print is_ascending(numbers1)
#print is_ascending(numbers2)

#list = [0, 1]
#times = 40
#
#while times > 0:
#    list.append(list[-1] + list[-2])
#    times -= 1
#    print list