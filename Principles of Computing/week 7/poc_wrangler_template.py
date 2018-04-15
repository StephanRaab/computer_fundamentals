"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    init_word = None
    for word in list1:
        if word != init_word:
            init_word = word
            new_list.append(word)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    counter = 0
    intersect_list = []
    add_elem = intersect_list.append
    len1 = len(list1)
    len2 = len(list2)
    
    if len1 < len2:
        list1, list2 = list2, list1
        len2 = len1
    for val in list1:
        while counter < len2 and list2[counter] < val:
            counter += 1
        if counter < len2:
            if val == list2[counter]:
                add_elem(val)
        else:
            break
    return intersect_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
        merge_list = []
    
    list1_count = 0
    list2_count = 0
    while list1_count < len(list1) and list2_count < len(list2):
        word1 = list1[list1_count]
        word2 = list2[list2_count]
        if word1 <= word2:
            merge_list.append(word1)
            list1_count += 1
        elif word2 < word1:
            merge_list.append(word2)
            list2_count += 1
    
    if list1_count < len(list1):
        return merge_list + list1[list1_count:]
    
    if list2_count < len(list2):
        return merge_list + list2[list2_count:]
    
    return merge_list
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    return []

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    