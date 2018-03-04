import math

#PERMUTATIONS

#lottery - 59 balls, draw 6 and order IS important
# m! / (m-n)!

print math.factorial(59)/math.factorial(59-6)

#this does the same thing
num_perms = 1
for idx in range(59, 59 - 6, -1):
    num_perms *= idx
print num_perms

# COMBINATIONS
# m!/(m-n)!*n!

print num_perms / math.factorial(6)