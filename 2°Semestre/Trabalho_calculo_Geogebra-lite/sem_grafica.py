#40*x – 2**(x**2) – 7 (certo)
#sen(x) – 3**x(Certo)
#x**3 – x – 1(Certo)
#2**x + x(Certo)
#8*x + log(x)(Certo)
from fractions import Fraction
from sympy import *
from cmath import *
import cmath
import numpy as np

class Sla():
    def __init__(self):
        while True:
            self.func = input("função : ")
            while True:
                a = Fraction(input("Digite a estimativa inicial a: "))
                self.fi = self.funcao(a)
                print(f'f(a) = {self.fi}')
                b = Fraction(input("Digite a estimativa inicial b: "))
                self.fb = self.funcao(b)
                print(f'f(b) = {self.fb}')
                me=min(a,b)
                ma=max(a,b)
                input("seguir")
                ac=False
                while True:
                    if me>=ma:
                        break
                    va=me
                    me+=0.3
                    self.fi = self.funcao(va)
                    fd = self.funcao(me)
                    if fd.real * self.fi.real <0:
                        if fd.imag and self.fi.imag:
                            break
                        else:
                            raiz = self.encontrar_raiz(float(va), float(me))
                            print(f"raiz entre {me} e {va}")
                            print(f"A raiz  da função é aproximadamente {raiz:.20f}.\n")
                            ac= True
                if ac:  
                    break
                else:
                    print(f"Os valores de f(a) e f(b) estao fora da possivel raiz da função {self.func}. Tente novamente.")
                    continue
            s=input("deseja continuar (s para sair)")
            if s=="s":
                break
            
    def funcao(self, x): 
        if np.all(x == 0):
            x = -0.00000000001
        todas_fun = {'x': x, 
    'sin': cmath.sin,
    'sen': cmath.sin,
    'cos': cmath.cos,
    'tan': cmath.tan,
    'asin': cmath.asin,
    'acos': cmath.acos,
    'atan': cmath.atan,
    'sinh': cmath.sinh,
    'cosh': cmath.cosh,
    'tanh': cmath.tanh,
    'asinh': cmath.asinh,
    'acosh': cmath.acosh,
    'atanh': cmath.atanh,
    'log': cmath.log10,
    'e': cmath.exp(1),
    'raiz': cmath.sqrt,
    'π': cmath.pi, 
    'pi': cmath.pi,
    'ln': cmath.log,}
        return  eval(self.func,todas_fun)
    def encontrar_raiz(self, a, b):
        cnt = 0
        c = 0
        erro=0.000000001
        while True:
            c = (a + b) / 2

            fc = self.funcao(c)
            e = b - a
            if abs(e) < erro:
                break
            if self.fi.real * fc.real < 0:
                b = c

            else:
                a = c
            cnt += 1
            if cnt > 5000:
                break
        print(f'Iteração {cnt}: a = {a:.20f}, b = {b:.20f}, error = {abs(e):.11f}')
        return c
Sla()
