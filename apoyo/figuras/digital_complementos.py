"""Figuras para el capitulo de complementos de control digital
(implementacion practica) -- PID discreto, dead-beat, cuantizacion.
No sale del cuaderno.

    python3 digital_complementos.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import control as ct


def pid_discreto(nombre='pid_discreto'):
    """Simulacion de PID discreto (ecuacion en diferencias, forma
    posicional) sobre una planta discreta de primer orden."""
    a, b = 0.8, 0.2
    T = 0.1
    Kp, Ki, Kd = 2.0, 1.5, 0.1
    N = 80
    r = 1.0
    y = np.zeros(N); u = np.zeros(N); e = np.zeros(N)
    integral = 0.0
    for k in range(1, N):
        e[k] = r - y[k-1]
        integral += e[k]
        deriv = (e[k] - e[k-1]) / T
        u[k] = Kp*e[k] + Ki*T*integral + Kd*deriv
        y[k] = a*y[k-1] + b*u[k-1]

    t = np.arange(N) * T
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.0), sharex=True)
    a1.axhline(r, color='0.7', lw=1, ls='--')
    a1.step(t, y, color='black', lw=1.2, where='post')
    a1.set_ylabel('$y(k)$')
    a2.step(t, u, color='black', lw=1.2, where='post')
    a2.set_ylabel('$u(k)$')
    a2.set_xlabel('$t=kT$ [s]')
    for ax in (a1, a2):
        ax.grid(True, ls=':', lw=0.5, color='0.85')
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def deadbeat(nombre='deadbeat'):
    """Respuesta al escalon del diseno dead-beat: T(z)=1/z, llega exacto
    a la referencia en una sola muestra."""
    G = ct.tf([0.5], [1, -0.5], dt=1)
    Gc = ct.tf([2, -1], [1, -1], dt=1)
    T = ct.feedback(Gc*G, 1)
    t, y = ct.step_response(T, np.arange(0, 8))

    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    ax.axhline(1, color='0.7', lw=1, ls='--', label='referencia')
    ax.step(t, y, color='black', lw=1.4, where='post', marker='o', ms=4)
    ax.set_xlabel('$k$ (muestras)')
    ax.set_ylabel('$y(k)$')
    ax.set_title('Dead-beat: $Y(z)/R(z)=z^{-1}$')
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def cuantizacion(nombre='cuantizacion'):
    """Ilustra el efecto de cuantizacion de un ADC de pocos bits sobre una
    señal senoidal."""
    t = np.linspace(0, 1, 2000)
    x = np.sin(2*np.pi*2*t)

    bits = 3
    niveles = 2**bits
    paso = 2/niveles
    xq = np.round(x/paso)*paso
    xq = np.clip(xq, -1, 1-paso)

    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ax.plot(t, x, color='0.6', lw=1.2, label='señal continua')
    ax.step(t, xq, color='black', lw=1.1, where='post', label=f'cuantizada ({bits} bits)')
    ax.set_xlabel('$t$')
    ax.set_ylabel('amplitud')
    ax.legend(fontsize=8, frameon=False, loc='lower right')
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    pid_discreto()
    deadbeat()
    cuantizacion()
