class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print('Point created')

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end
        print('Line created')

    def __str__(self) -> str:
        return f'{self.start} -> {self.end}'

class PointFactory:
    def create_point(self, x, y):
        return Point(x, y)

class LineFactory:
    def create_line(self, start, end):
        return Line(start, end)

# singleton decorator
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

@singleton
class SingletonPointFactory:
    def create_point(self, x, y):
        return Point(x, y)

@singleton
class SingletonLineFactory:
    def create_line(self, start, end):
        return Line(start, end)

def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    factory1 = factory()
    factory2 = factory()
    return factory1 == factory2

if __name__ == '__main__':
    #print(is_singleton(PointFactory))
    print(is_singleton(SingletonPointFactory))
    #print(is_singleton(LineFactory))
    #print(is_singleton(SingletonLineFactory))