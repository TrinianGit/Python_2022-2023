# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print(str(self) + ',', x)

    @classmethod
    def class_foo(cls, x):
        print(str(cls) + ',', x)
    
    @staticmethod
    def static_foo(x):
        print(x)

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Abstract(ABC):
    
    @abstractmethod
    def abstract_method(self, x):
        return f"Wewnatrz klasy abstrakcyjnej, {x}"

class MyClass(Abstract):

    def abstract_method(self, x):
        print(self, x)
        print(super().abstract_method(x))

try:
    abst = Abstract()
    print(abst.abstract_method(19))
except Exception as err:
    print (err)

mc = MyClass()
mc.abstract_method(123)

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class Celsiusze:
    def __init__(self, temperatura=0):
        self.temperatura = temperatura

    def fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    @property
    def temperatura(self):
        print("temperatura.getter")
        return self._temperatura

    @temperatura.setter
    def temperatura(self, cel):
        print("temperatura.setter")
        if cel < -273.15:
            print("Temperatura poniżej -273 jest niemożliwa do osiągnięcia")
            return
        self._temperatura = cel
        
    @temperatura.deleter
    def temperatura(self):
        print (f"Usuwanie temperatury obiektu {self}")
        del self._temperatura

t1 = Celsiusze(37)

print(t1.temperatura)

print(t1.fahrenheit())

t2 = Celsiusze(-300)
print("-------------------")
print("Usuwanie  temp.  t1")
del t1.temperatura
print("-------------------")
try:
    print (t1.temperatura)
except Exception as err:
    print (err)
print("\n",t1)
print("-------------------")
print("Usuwanie obiektu t1")
del t1
print("-------------------")
try:
    print (t1)
except Exception as err:
    print (err)