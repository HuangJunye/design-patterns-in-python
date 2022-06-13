# singleton decorator
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

class Database:
    def __init__(self):
        print('Database created')

    def create_database():
        return Database()

    @singleton
    def create_database_singleton():
        return Database()

def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    factory1 = factory()
    factory2 = factory()
    return factory1 == factory2

if __name__ == '__main__':
    print(is_singleton(Database.create_database))
    print(is_singleton(Database.create_database_singleton))