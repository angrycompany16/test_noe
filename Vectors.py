from __future__ import print_function
import math
import builtins as __builtin__

class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) is not Vector2D:
            return Vector2D(self.x * other, self.y * other)
        else:
            return Vector2D(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def printVector(self, vector):
        __builtin__.print(vector.x, vector.y)

    def Normalize(self):
        oldVector = self
        # compute k
        k = math.sqrt(1 / (math.pow(self.x, 2) + math.pow(self.y, 2) ) )
        # compute the normalized vector with k
        return k * oldVector

