class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f'{self.start} -> {self.end}'

    def deep_copy(self):
        return Line(Point(self.start.x, self.start.y), Point(self.end.x, self.end.y))

if __name__ == "__main__":
    l1 = Line(Point(1, 2), Point(3, 4))
    l2 = l1.deep_copy()
    l2.start = Point(5, 6)
    print(l1)
    print(l2)