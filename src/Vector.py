
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self._x = self.x + other.x
        self._y = self.y + other.y

    def __abs__(self,x,y):
        pass

    def __mul__(self, scalar):
        self._x = self.x * scalar
        self._y = self.y * scalar

    def __repr__(self):
        return Vector(self._x,self._y)




if __name__ == "__main__":
    print(Vector(1,2)+Vector(2,3))