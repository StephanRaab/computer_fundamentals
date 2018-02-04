s = set([1,2,3,4])
t = set([3,4,5,6])

print s
#print t.symmetric_difference_update(s) NO
#print s.symmetric_difference_update(t) YES
#print s.update(s)                      NO
#print s.intersection(t)				NO
#print s.remove(4)						YES
#print t.intersection(s)				NO
# print(t.symmetric_difference(s)) #no
# print(s.update(t)) # yes
# print s.difference(t) #no
# print s.discard(4) # yes
# print t.update(s) # no
print s.intersection_update(s)
print s