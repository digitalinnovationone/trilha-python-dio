class Foo:
    def __init__(self, x=None):
        self._x = x
# o @property me ajuda com que eu acesse o atributo e não a sintasse
    @property
    def x(self):
        return self._x or 0
# para ativuir um novo valor a propriedade, preciso ter o setter e antes acionar o valor de X la do inicio.
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
