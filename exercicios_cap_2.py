# -*- coding: utf-8 -*-
from scipy import *
from matplotlib.pyplot import *
from numpy import *
import cmath
import math
#exercício: Check whether x = 2.3 is a zero of the function: f(x)=x^2+0.25x-5
print("Exercício 1: \n")
x = 2.3
def f(x):
    return x**2+0.25*x-5
if f(x) != 0:
    print("Não é um zero da função")
else:
    print("É um zero da função \n")

#exercício: According to de Moivre's formula, the following holds: 
#(cosx+isinx)^n=cosnx+isinnx para n pertencendo a Z e x pertencendo a R
#Choose numbers n and x and verify that formula in Python
print("Exercício 2: \n")
n = 5
x = 3.
#Definiremos os dois lados da função como funções diferentes e depois comparamos elas
def f(x):
    return (math.cos(x)+math.sin(x)*1j)**n
def g(x):
    return math.cos(n*x)+math.sin(n*x)*1j
if cmath.isclose(f(x),g(x)):
    print("A fórmula é verdadeira")
else:
    print("A fórmula é falsa")
print(f(x))
print(g(x)) 

#exercicio: Complex numbers. Verify Euler's formula in the same way: e^ix=cosx+isinx
print("Exercício 3: \n")
x=3.
if exp(x*1j) == math.cos(x)+math.sin(x)*1j:
    print("A fórmula de Euler é verdadeira \n")
else:
    print("A fórmula de Euler é falsa \n")

#exercicio: Suppose we are trying to check the convergence of a diverging sequence (here the
#sequence is defined by the recursive relation un+1 = 2un and u0 = 1.0):
print("Exercício 4: \n")
u = 1. 
uold = 10.
for iteration in range(2000):
    if not abs(u-uold) > 1.e-8:
        print('Convergence')
        break 
    uold = u
    u = 2*u
else:
    print('No convergence') 


#exercicio: An implication C = (A ⇒ B) is a Boolean expression that is defined as
#C is True if A is False or A and B are both True
#C is False otherwise
print("Exercício 5: \n")
A = False
B = False
if A == False or A and B == True:
    print("C é verdadeiro \n")
else:
    print("C é falso \n")
    
#exercicio: This exercise is to train Boolean operations. Two binary digits (bits) are added by
#using a logical device called a half adder. It produces a carry bit (the digit of the next higher
#value) and the sum as defined by the following table, and half adder circuit.
print("Exercício 6: \n")
p = 0
q = 1
if p or q:
    s = 1
else:
    s = 0
if p and q:
    c = 1
else:
    c = 0
print(s, c)
#esse é o half adder
p = 0
q = 1
if p or q:
    if p or q:
        s = 1
    else:
        s = 0
    if p and q:
        c = 1
    else:
        c = 0
else:
    s = 0
if p and q:
    c = 1
else:
    c = 0
print(s, c)
