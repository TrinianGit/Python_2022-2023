from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x):
        self.x = x

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    print(f"Pole: Prostokąt")
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
# funkcja pole, najpierw przypisz argumenty do x, y instancji, potem policz pole powierzchni
def pole(instance: Prostokat, a, b):
    instance.x = a
    instance.y = b
    print(f"Pole: Prostokąt")
    return instance.x * instance.y

@dispatch(Kwadrat)
# funkcja pole
def pole(instance: Kwadrat):
    print(f"Pole: Kwadrat")
    return instance.x ** 2

@dispatch(Kwadrat, int)
# funkcja pole z podanym argumentem boku
def pole(instance: Kwadrat, a):
    instance.x = a
    print(f"Pole: Kwadrat")
    return instance.x ** 2

# testy

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i)) # polymorphism at runtime

polaPowierzchni([a,b,c])