class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id} {self.name}'

class PersonFactory:
    current_id = -1

    def create_person(self, name):
        self.current_id += 1
        return Person(self.current_id, name)

if __name__=="__main__":
    factory = PersonFactory()
    p1 = factory.create_person('John')
    p2 = factory.create_person('Jane')
    print(p1)
    print(p2)