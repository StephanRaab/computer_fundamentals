"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for answer in answer_set:
            for item in outcomes:
                new_sequence = list(answer)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    #based this off of max_repeats(seq)
    return max([points * hand.count(points) for points in set(sorted(hand))])

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    
    - Cycle through the generated rolls
    - Pass them to a new list
    - Use sum to total all the values
    - Return expected value by dividing the sum by the length (avg)
    """
    total_rolls = gen_all_sequences([num + 1 for num in range(num_die_sides)], num_free_dice)
    new_rolls = [] 
    for roll in total_rolls:
        new_rolls.append(roll + held_dice)
    results = [score(die) for die in new_rolls]
    return sum(results) / float(len(results))

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = set([()])
    for dummy_i in range(len(hand)):
        temp_set = set()
        for item in all_holds:
            new_sequence = list(item)
            new_sequence.append(hand[dummy_i])
            temp_set.add(tuple(new_sequence))
        all_holds = all_holds.union(temp_set)
    return all_holds

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    
    - Generate all the available holds
    - Iterate through the holds
    - Pass the dice that I'm holding to the expected_value to get the score value
    - Pass the expected_value to the result dictionary
    - Cycle through to get the maximum/best value
    """
    all_holds = gen_all_holds(hand)
    results = dict()
    for hold in all_holds:
        free_dice = len(hand) - len(hold)
        e_val = expected_value(hold, num_die_sides, free_dice)
        results[e_val] = hold
    max_value = max([value for value in results])
    return (max_value, results[max_value])

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
        
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
#import expected_value_testsuite
#expected_value_testsuite.run_suite(expected_value)
#import score_testsuite
#score_testsuite.run_suite(score)
#import gen_all_holds_testsuite
#gen_all_holds_testsuite.run_suite(gen_all_holds)
#import strategy_testsuite
#strategy_testsuite.run_suite(strategy)