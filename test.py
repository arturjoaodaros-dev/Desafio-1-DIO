def x():
    print('x')
y = x
y()
print(x is y)
def y():
    print('y')

def executar(func):
    def execução():
        print('log:', func.__name__)
        func()
    return execução
i = executar(y)
i()


@executar
def z():
    print('z')
z()
print('===================================================================')
class Foo:
    def __init__(self) -> None:
        self.x = [1,2,3,4,5,6,7,8,9]
        self.index = 0
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index >= len(self.x):
            raise StopIteration
        v = self.x[self.index]
        self.index += 1
        return v
for i in Foo():
    print(i)
print('===================================================================')

def contar():
    for i in range(0, 1000):
        yield i

g = contar()
print(next(g))
print(next(g))
print(next(g))
print(g)
print(contar())
print(x is y)