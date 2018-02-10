"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    first_list = []
    for num in line:
        if num  > 0:
            first_list.append(num)
    if len(first_list) < len(line):
        add_zero = len(line) - len(first_list)
        for num in range(add_zero):
            first_list.append(0)
         
    for num in range(1, len(line)):
        if first_list[num - 1] == first_list[num]:
            first_list[num - 1] *= 2
            first_list[num] = 0
    
    final_list = []
    for num in first_list:
        if num > 0:
            final_list.append(num)
    if len(final_list) < len(line):
        add_zero = len(line) - len(final_list)
        for num in range(add_zero):
            final_list.append(0)
            
    return final_list