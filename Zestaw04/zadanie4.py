from functools import singledispatch
from typing import Union

@singledispatch
def func(arg1):
    print(f"Argument funkcji jest typu: {type(arg1)}. To domyślne działanie")

@func.register
def _(arg1: int):
    print(f"Argument funkcji jest typu: {type(arg1)}. Ten typ jest przystosowany do operacji arytmetycznych")

@func.register
def _(arg1: float):
    print(f"Argument funkcji jest typu: {type(arg1)}. Ten typ jest przystosowany do operacji arytmetycznych")

@func.register
def _(arg1: str):
    print(f"Argument funkcji jest typu: {type(arg1)}. Ten typ nie jest przystosowany do operacji arytmetycznych")



func(12)
func(1.12)
func("Ok")
func((1 + 12j))


from functools import singledispatchmethod

class Printer:
    @singledispatchmethod
    def mth(self, arg1):
        print(f"Wywołane z obiektu klasy: {self}. Argument funkcji jest typu: {type(arg1)}. To domyślne działanie")

    @func.register
    def _(self, arg1: int):
        print(f"Wywołane z obiektu klasy: {self}. Argument funkcji jest typu: {type(arg1)}. Ten typ jest przystosowany do operacji arytmetycznych")

    @func.register
    def _(self, arg1: float):
        print(f"Wywołane z obiektu klasy: {self}. Argument funkcji jest typu: {type(arg1)}. Ten typ jest przystosowany do operacji arytmetycznych")

    @func.register
    def _(self, arg1: str):
        print(f"Wywołane z obiektu klasy: {self}. Argument funkcji jest typu: {type(arg1)}. Ten typ nie jest przystosowany do operacji arytmetycznych")

p = Printer()
p.mth(11)
p.mth(243.43)
p.mth("Hello")
p.mth((11 + 12j))