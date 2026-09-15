"""Equivalente en Python de clase2.m

Original (MATLAB):
    s = tf('s');
    g = (s+3)/[(s+2)*(s^2+s+8)]
    k = 386
    Td = 1000;
    Ti = 900;

    gc = k*[1+(1/Ti)*(1/s)+Td*s]
    T = feedback(gc*g,1)
    ltiview(T)

Traduccion literal de las ganancias originales del script de clase.
(La critica de esta sintonia -- por que Kd=386000 es un problema, y una
sintonia alternativa disenada -- esta en el capitulo 05 de los apuntes,
no aqui: este archivo es la traduccion fiel del .m, no la version
narrada.)
"""
import control as ct
import matplotlib.pyplot as plt
import numpy as np

s = ct.tf('s')
g = (s + 3) / ((s + 2) * (s**2 + s + 8))

k = 386
Td = 1000
Ti = 900

gc = k * (1 + (1/Ti)*(1/s) + Td*s)
T = ct.feedback(gc*g, 1)
print(T)

print("polos de lazo cerrado:", np.round(T.poles(), 6))
print("ganancia de DC:", ct.dcgain(T))

if __name__ == '__main__':
    t = np.linspace(0, 6, 3000)
    t, y = ct.step_response(T, t)
    plt.plot(t, y)
    plt.xlabel('t [s]')
    plt.ylabel('y(t)')
    plt.title('Respuesta al escalón del lazo cerrado (PID de clase)')
    plt.grid(True, ls=':')
    plt.show()
