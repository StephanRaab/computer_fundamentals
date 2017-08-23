# Remainder - modular arithmetic
#
# problem: get the ones digit of a number

num = 27
tens =  num // 10
ones = num % 10
print tens, ones
print 10 * tens + ones, num

# Clock arithmetic
current_time = 17
shift = 8

print (current_time + shift) % 24

# application - screen wraparound
# spaceship from week 7 example
print "========================"
width = 800
position = 797
print "Your position is: " + str(position)
move = 7
print "You moved by: " + str(move)
position = (position + move) % width
print "Your new position is now: " + str(position)

# Convert hour format to 24-hour format
print "======================="

hour = 7
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens) + str(ones) + ":00"
