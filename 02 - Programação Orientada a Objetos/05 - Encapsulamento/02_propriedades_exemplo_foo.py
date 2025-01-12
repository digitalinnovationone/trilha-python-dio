class Foo:
    def __init__(self, x=None):
        self.__x = x

    @property
    def x(self):
        return self.__x or 0

    @x.setter
    def x(self, value):
        self.__x += value

    @x.deleter
    def x(self):
        self.__x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
