class Overload():
    def __init__(self, param1):
        pass
    
    def __init__(self, param1, param2):
        pass
    
object1 = Overload(2)
print object1

object2 = Overload(2, 3)
print object2