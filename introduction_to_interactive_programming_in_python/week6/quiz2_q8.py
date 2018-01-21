slow_wumpus = 1000
slow_death = 0.4
fast_wumpus = 1
fast_death = 0.3

count = 2
total_years = 57

while count < total_years:
    print "year:", count
    slow_wumpus += slow_wumpus
    slow_wumpus -= slow_wumpus * slow_death
    print "slow:", slow_wumpus
    fast_wumpus += fast_wumpus
    fast_wumpus -= fast_wumpus * fast_death
    print "fast:", fast_wumpus
    if fast_wumpus > slow_wumpus:
        print "bigger"
    else:
        print "smaller"
    print""
    count += 1