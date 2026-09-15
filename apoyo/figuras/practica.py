"""Figuras de los capitulos practicos (modelado fisico, instrumentacion y
proyecto integrador). No salen del cuaderno.

    python3 practica.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Parametros del motor DC que se usa como hilo conductor
K_MOTOR, TAU_MOTOR = 22.07, 0.01471
T_S = 0.005          # periodo de muestreo elegido
RES_ENC = 0.628      # resolucion de velocidad del encoder [rad/s]


def _limpiar(ax):
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)


def linealizacion(nombre='linealizacion'):
    """Tanque con valvula: q_out = k*sqrt(h) y su recta tangente en dos
    puntos de operacion distintos."""
    k = 0.02
    h = np.linspace(0, 6, 400)
    q = k*np.sqrt(h)

    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    ax.plot(h, q, color='black', lw=1.5, label=r'$q_{out}=k\sqrt{h}$ (real, no lineal)')

    for h0, estilo in ((1.0, '--'), (4.0, ':')):
        q0 = k*np.sqrt(h0)
        pend = k/(2*np.sqrt(h0))
        hh = np.linspace(h0-1.2, h0+1.2, 10)
        ax.plot(hh, q0 + pend*(hh-h0), color='0.45', lw=1.1, ls=estilo)
        ax.plot([h0], [q0], marker='o', ms=5, color='black')
        ax.annotate(f'$h_0={h0:.0f}$ m\n$R={2*np.sqrt(h0)/k:.0f}$ s/m$^2$',
                    (h0, q0), textcoords='offset points', xytext=(6, -22),
                    fontsize=8)

    ax.set_xlabel('$h$ [m]')
    ax.set_ylabel('$q_{out}$ [m$^3$/s]')
    ax.set_title('Linealización en el punto de operación')
    ax.legend(fontsize=8, frameon=False, loc='upper left')
    _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def pwm(nombre='pwm'):
    """Señal PWM y su valor medio: el 'DAC' que realmente se usa."""
    f_pwm = 20.0
    t = np.linspace(0, 0.2, 4000)
    D = 0.65
    Vcc = 12.0
    onda = Vcc*((t*f_pwm) % 1.0 < D)

    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    ax.plot(t*1000, onda, color='black', lw=1.1, label='PWM')
    ax.axhline(D*Vcc, color='0.45', lw=1.3, ls='--',
               label=f'valor medio $D\\,V_{{cc}}$ = {D*Vcc:.1f} V')
    ax.set_xlabel('$t$ [ms]')
    ax.set_ylabel('$v$ [V]')
    ax.set_ylim(-1, Vcc+2)
    ax.legend(fontsize=8, frameon=False, ncol=2, loc='upper right')
    _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def filtro_ema(nombre='filtro_ema'):
    """Filtro exponencial de primer orden sobre una medida ruidosa, con dos
    valores de alpha: el compromiso ruido/retardo."""
    rng = np.random.default_rng(7)
    N = 200
    t = np.arange(N)*T_S
    limpio = 100*(1-np.exp(-t/0.05))
    medido = limpio + rng.normal(0, 6, N)

    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    ax.plot(t, medido, color='0.75', lw=0.9, label='medida cruda')
    for alpha, estilo in ((0.5, '-'), (0.1, '--')):
        y = np.zeros(N)
        for k in range(1, N):
            y[k] = alpha*medido[k] + (1-alpha)*y[k-1]
        ax.plot(t, y, color='black', lw=1.2, ls=estilo,
                label=f'EMA $\\alpha={alpha}$')
    ax.plot(t, limpio, color='0.4', lw=1.0, ls=':', label='valor real')
    ax.set_xlabel('$t$ [s]')
    ax.set_ylabel(r'$\omega$ [rad/s]')
    ax.set_title('Filtro exponencial: menos ruido = más retardo')
    ax.legend(fontsize=8, frameon=False, loc='lower right')
    _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def identificacion(nombre='identificacion_motor'):
    """Ensayo de escalon del motor con ruido y cuantizacion del encoder, y
    el ajuste de K y tau por minimos cuadrados."""
    rng = np.random.default_rng(3)
    t = np.arange(0, 0.25, T_S)
    V = 6.0
    real = K_MOTOR*V*(1-np.exp(-t/TAU_MOTOR))
    medido = np.round((real + rng.normal(0, 0.4, t.size))/RES_ENC)*RES_ENC

    def modelo(t, K, tau):
        return K*V*(1-np.exp(-t/tau))

    (Kf, tauf), _ = curve_fit(modelo, t, medido, p0=[10, 0.05])

    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    ax.plot(t*1000, medido, ls='none', marker='o', ms=3.5, mfc='none',
            mec='0.35', label='medido (encoder)')
    ax.plot(t*1000, modelo(t, Kf, tauf), color='black', lw=1.4,
            label=f'ajuste: $K$={Kf:.1f}, $\\tau$={tauf*1000:.1f} ms')
    ax.axhline(Kf*V, color='0.6', lw=0.8, ls='--')
    ax.axvline(tauf*1000, color='0.6', lw=0.8, ls=':')
    ax.annotate(r'$0.632\,K V$ en $t=\tau$', (tauf*1000, 0.632*Kf*V),
                textcoords='offset points', xytext=(10, -6), fontsize=8)
    ax.set_xlabel('$t$ [ms]')
    ax.set_ylabel(r'$\omega$ [rad/s]')
    ax.set_title('Identificación experimental del motor')
    ax.legend(fontsize=8, frameon=False, loc='lower right')
    _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def proyecto_lazo(nombre='proyecto_lazo'):
    """Validacion del proyecto integrador: lazo digital completo con PI
    incremental, cuantizacion del encoder y saturacion del driver."""
    Kp, Ki = 0.0294, 2.0
    a = np.exp(-T_S/TAU_MOTOR)
    b = K_MOTOR*(1-a)
    N = 60
    r = 150.0
    w = np.zeros(N); u = np.zeros(N); e = np.zeros(N)
    for k in range(1, N):
        wq = np.round(w[k-1]/RES_ENC)*RES_ENC
        e[k] = r - wq
        du = Kp*(e[k]-e[k-1]) + Ki*T_S*e[k]
        u[k] = np.clip(u[k-1] + du, 0, 12)
        w[k] = a*w[k-1] + b*u[k-1]

    t = np.arange(N)*T_S*1000
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.0), sharex=True)
    a1.axhline(r, color='0.65', lw=1.0, ls='--', label='referencia')
    a1.axhspan(0.98*r, 1.02*r, color='0.9', label='banda ±2 %')
    a1.step(t, w, color='black', lw=1.3, where='post')
    a1.set_ylabel(r'$\omega$ [rad/s]')
    a1.legend(fontsize=8, frameon=False, loc='lower right')
    a2.step(t, u, color='black', lw=1.3, where='post')
    a2.axhline(12, color='0.65', lw=1.0, ls=':')
    a2.annotate('límite del driver (12 V)', (t[-1], 12),
                textcoords='offset points', xytext=(-95, 4), fontsize=8,
                color='0.35')
    a2.set_ylabel('$u$ [V]')
    a2.set_xlabel('$t$ [ms]')
    a2.set_ylim(0, 14)
    for ax in (a1, a2):
        _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    linealizacion()
    pwm()
    filtro_ema()
    identificacion()
    proyecto_lazo()
