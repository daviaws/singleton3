class MetaSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        singleton = type(instance)
        if not singleton in MetaSingleton._instances:
            MetaSingleton._instances[singleton] = {}
        instances = MetaSingleton._instances[singleton]
        if instance not in instances:
            instances[instance] = instance
        return instances[instance]

class Cood(metaclass=MetaSingleton):

    def __init__(self, x, y):
        self.id = hash((x, y))
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Cood):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.id

    def __repr__(self):
        return "Cood: ({}, {})".format(self.x, self.y)

a = Cood(1, 1)
b = Cood(1, 1)
c = Cood(1, 2)
print(a)
print(b)
print(c)
print(a is b)
print(a is b is c)
