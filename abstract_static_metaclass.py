import abc

class StaticClassError(Exception):
    pass


class StaticClass:
    __metaclass__ = abc.ABCMeta

    def __new__(cls, *args, **kw):
        raise StaticClassError("%s is a static class and cannot be initiated."
                                % cls)

class MyClass(StaticClass):
    a = 1
    b = 3

    @staticmethod
    def add(x, y):
        return x+y


if __name__ == '__main__':
    print "A", MyClass.a
    print "B", MyClass.b
    print MyClass.add(3,4)
    print
    my_class = MyClass()
