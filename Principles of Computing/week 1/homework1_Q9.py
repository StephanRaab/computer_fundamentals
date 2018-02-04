def appendsums(lst):
    """
    repeatedly append the sum of the current last three elements
    of lst to lst.
    """
    for count in range(25):
        lst.append(lst[-1] + lst[-2] + lst[-3])
        print lst
        
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]
