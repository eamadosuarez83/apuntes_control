"""Equivalente en Python del archivo "clase3" (sin extension).

Original (MATLAB):
    clc
    clear all;
    close all;
    syms s
    g=1/(s^2+4);
    x=1/s;
    y=g*x;
    yt=ilaplace(y)
"""
import sympy as sp

s, t = sp.symbols('s t', positive=True)

g = 1/(s**2 + 4)
x = 1/s
y = g*x
yt = sp.simplify(sp.inverse_laplace_transform(y, s, t))

if __name__ == '__main__':
    print("g(s) =", g)
    print("y(s) = g(s)*x(s) =", y)
    print("y(t) =", yt)
