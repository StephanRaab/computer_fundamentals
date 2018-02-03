count = set([])

def next(x):
    return (x ** 2 + 79) % 997

x = 1
for i in range(1000):
    count.add(x)
    x = next(x)
    
print len(count)