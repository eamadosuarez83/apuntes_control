"""Equivalente en Python de clase1.m

Original (MATLAB):
    s = tf('s');
    g = (s)/[(s+2)*(s^2+s+8)]
    ltiview(g)

Nota de traduccion: los corchetes en (s+2)*(s^2+s+8)] son concatenacion
de matrices en MATLAB, no agrupacion -- funcionan aqui solo porque
concatenar un unico elemento devuelve ese elemento. En Python van
parentesis normales.

ltiview() abre un panel interactivo (step, bode, etc.); el equivalente
mas directo en Python es step_response() + matplotlib.
"""
import control as ct
import matplotlib.pyplot as plt
import numpy as np

s = ct.tf('s')
g = s / ((s + 2) * (s**2 + s + 8))
print(g)

print("polos:", g.poles())
print("ceros:", g.zeros())
print("ganancia de DC:", ct.dcgain(g))

if __name__ == '__main__':
    t = np.linspace(0, 12, 1000)
    t, y = ct.step_response(g, t)
    plt.plot(t, y)
    plt.xlabel('t [s]')
    plt.ylabel('y(t)')
    plt.title('Respuesta al escalón de g(s)')
    plt.grid(True, ls=':')
    plt.show()
