"""Equivalente en Python de clase4.slx (modelo de Simulink).

clase4.slx no tiene codigo de texto: es un diagrama de bloques binario.
Los parametros de abajo se decodificaron leyendo el XML interno del
.slx (simulink/blockdiagram.xml, dentro del archivo zip), no se
adivinaron. Topologia real, con los SID de cada bloque:

    Step(4) ----------+--(ManualSwitch:7, in:1)--+
                       |                          |--> Sum(3, in:1 -- el
    RandomNumber(5) ---+--(ManualSwitch:7, in:2)--+     in:2 de Sum NO
                                                          esta cableado,
                                                          asi que Sum
                                                          es un simple
                                                          passthrough)
                        |
                        v
               Relay(6) --> LTI System(9): sys = tf(1,[1 1])  =  1/(s+1)
                        |
    Mux(8): in:1 = Step/Random (antes del relay), in:2 = salida de la
    planta  -->  Scope(2)

Parametros que SI estan explicitos en el .slx:
  - Planta:        G(s) = 1/(s+1)                    (tau = 1 s)
  - RandomNumber:  SampleTime = 0.1 s                 (Mean=0, Variance=1
                    son los valores por defecto de Simulink, no estan
                    sobreescritos en el XML)
  - Step:          SampleTime = 0                     (StepTime=1,
                    Initial=0, Final=1 son los valores por defecto)
  - Relay:         no tiene parametros propios en el XML -> toma los
                    valores por defecto de Simulink: Switch on point = 1,
                    Switch off point = 1, Output on = 1, Output off = 0.
  - ManualSwitch:  la posicion guardada no aparece como parametro
                    explicito -> por defecto selecciona la entrada 1
                    (Step). Es el interruptor que el profesor movia en
                    vivo durante la clase para pasar de la entrada limpia
                    a la ruidosa.

No hay realimentacion: el in:2 de Sum quedo sin cablear, asi que esto
NO es un lazo cerrado con referencia e histeresis (a diferencia de la
figura clase4_onoff_ruido.svg del capitulo 05, que es una ilustracion
didactica de proposito general, no una reconstruccion de este .slx en
particular -- esa se deja igual, sin tocar).

Observacion, no un bug de esta traduccion: con el switch en la posicion
por defecto (Step) y los umbrales por defecto del Relay (on = off = 1),
el escalon se queda parado EXACTO en el umbral (Final value = 1) y el
Relay entra en "chattering": conmuta en cada paso de simulacion, porque
"on" y "off" comparten el mismo valor y la entrada nunca lo cruza, solo
lo toca. Es el motivo mas probable por el que en clase se pasaba el
ManualSwitch a la rama de ruido: ahi la señal SI cruza el umbral de forma
limpia y el rele conmuta como un comparador normal.
"""
import numpy as np
import matplotlib.pyplot as plt

TAU, K = 1.0, 1.0          # G(s) = 1/(s+1)
ON_POINT = OFF_POINT = 1.0  # valores por defecto del bloque Relay
OUT_ON, OUT_OFF = 1.0, 0.0
DT = 0.001


def simular(entrada, T=6.0, dt=DT):
    """entrada: funcion u(t) -> escalar. Devuelve t, u, v (salida del
    relay) y (salida de la planta)."""
    N = int(T/dt)
    t = np.arange(N)*dt
    a = np.exp(-dt/TAU)
    b = K*(1 - a)

    u = np.array([entrada(tk) for tk in t])
    v = np.zeros(N)
    y = np.zeros(N)
    estado = 0
    for k in range(1, N):
        uk = u[k-1]
        if estado == 0 and uk >= ON_POINT:
            estado = 1
        elif estado == 1 and uk <= OFF_POINT:
            estado = 0
        v[k-1] = OUT_ON if estado else OUT_OFF
        y[k] = a*y[k-1] + b*v[k-1]
    return t, u, v, y


def entrada_step(t):
    """Step por defecto de Simulink: StepTime=1, Initial=0, Final=1."""
    return 1.0 if t >= 1.0 else 0.0


def entrada_random(seed=0, sample_time=0.1):
    """RandomNumber por defecto: Mean=0, Variance=1, muestreado cada
    0.1 s (el unico parametro que SI viene explicito en el .slx)."""
    rng = np.random.default_rng(seed)
    cache = {}

    def u(t):
        k = int(t / sample_time)
        if k not in cache:
            cache[k] = rng.normal(0, 1)
        return cache[k]
    return u


if __name__ == '__main__':
    fig, axes = plt.subplots(2, 2, figsize=(9, 5), sharex='col')

    t, u, v, y = simular(entrada_step)
    axes[0][0].plot(t, u, label='u (Step)')
    axes[0][0].plot(t, y, label='y (planta)')
    axes[0][0].set_title('ManualSwitch en Step (posición por defecto)\n'
                          '-> chattering del relay en t>1s')
    axes[0][0].legend(fontsize=8)
    axes[1][0].plot(t, v, color='0.3')
    axes[1][0].set_ylabel('v (salida del Relay)')
    axes[1][0].set_xlabel('t [s]')

    t, u, v, y = simular(entrada_random())
    axes[0][1].plot(t, u, label='u (Random Number)')
    axes[0][1].plot(t, y, label='y (planta)')
    axes[0][1].set_title('ManualSwitch en Random Number\n'
                          '-> el relay conmuta con normalidad')
    axes[0][1].legend(fontsize=8)
    axes[1][1].plot(t, v, color='0.3')
    axes[1][1].set_xlabel('t [s]')

    fig.tight_layout()
    plt.show()
