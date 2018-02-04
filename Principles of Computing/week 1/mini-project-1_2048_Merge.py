"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    first_list = []
    second_list = []
    final_list = []
    
    for num in line:
        first_list.append(0)
        
    count = 0
    print "Before:", line
    for square in line:
        if square > 0:
            first_list[count] = square
            count += 1
        else:
            count = count
    print "First: ", first_list
    
    mergeTotal = len(line) / 2
    mergeAmount = 0
    for item in range(len(first_list)-1):
        print first_list[item], ":", first_list[item + 1]
        if (first_list[item] == first_list[item + 1]) and mergeAmount < mergeTotal :
            second_list.append(first_list[item] + first_list[item + 1])
            second_list.append(0)
            mergeAmount += 1
#        elif mergeAmount == mergeTotal:
#            second_list.append(first_list[item])
#        else:
#            second_list.append(first_list[item])
            
    print "Second:", second_list
    
    final_count = 0
    for num in line:
        final_list.append(0)
        
    for number in second_list:  
        if number > 0:
            final_list[final_count] = number
            final_count += 1
        else:
            final_count = final_count
                 
    print "Final:", final_list
    return final_list

merge([2, 2, 2, 2])