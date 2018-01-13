list = [1, 82, -6, 4, 3, 8]
if 1 in list:
    print(':D')
else:
    print(':(')

print(str(list.index(4)))

print('The List: ' + str(list))

list.append(5)
print('Appending 5: ' + str(list))

list.pop()

print(str(list.pop()))

print('Popping 5: ' + str(list))