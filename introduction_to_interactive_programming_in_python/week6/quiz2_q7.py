n = 100
numbers = range(2, n)
result = [2]
for i in numbers:
    even = False
    for j in result:
        if i % j == 0:
            even = True
            break
    if even == False:
        result.append(i)
print result
print len(result)