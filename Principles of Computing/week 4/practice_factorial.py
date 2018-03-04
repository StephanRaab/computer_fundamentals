import math
print math.factorial(4)

def sr_factorial(factor):
    ans = 1
    for i in range(1, factor +1):
        ans *= i
    print ans
    
sr_factorial(4)