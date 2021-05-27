class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if type(other) is not Vector2D:
            return Vector2D(self.x * other, self.y * other)
        else:
            return Vector2D(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return Vector2D(self.x * other, self.y * other)
