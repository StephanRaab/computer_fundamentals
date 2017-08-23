# prime number list
###################################################

prime_list = [2, 3, 5, 7, 11, 13]
print prime_list[1], prime_list[3], prime_list[5]

# ###################################################
# # Expected output
#
# #3 7 13

print ###########################################

# List reference problem
########################
a = [5, 3, 1, -1, -3, 5]

b = a

b[0] = 0

print("a: " + str(a))
print("b: " + str(b))

print ###########################################
# List Copy
a = [5, 3, 1, -1, -3, 5]

b = list(a)
b[0] = 0
print(a)
print(b)

print ###########################################
# Vector addition function
def add_vector(v, w):
    x = v[0] + w[0]
    y = v[1] + w[1]
    return [x, y]

print(add_vector([4, 3], [0,0]))
