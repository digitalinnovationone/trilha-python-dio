class Foo:
    def __init__(self, x=None):
        self._x = x

    @property  # transforma um método em um atributo
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
